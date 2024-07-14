from flask import Flask, request, jsonify
from package.base.app import webapp, commonBp
import time
import numpy as np
import faiss
from transformers import AutoTokenizer, AutoModel
import torch
import os


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


app = Flask(__name__)
modelsDir = os.path.abspath(os.path.join(__file__, '../../../models'))
miniLM = os.path.join(modelsDir, 'bert-base-chinese')
# 加载预训练模型和分词器
tokenizer = AutoTokenizer.from_pretrained(miniLM)
model = AutoModel.from_pretrained(miniLM)

# 全局变量，用于存储训练数据和Faiss索引
texts = []
ids = []
index = None

def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

@commonBp.route("/train")
def train():
    global texts, ids, index
    data = request.get_json()
    file_path = data.get('file_path')

    # 读取训练数据
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    texts = []
    ids = []
    embeddings = []

    start_time = time.time()

    for line in lines:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            id_, text = parts
            texts.append(text)
            ids.append(id_)
            embeddings.append(embed_text(text))

    embeddings = np.array(embeddings).astype("float32")

    # 构建Faiss索引
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    training_time = time.time() - start_time
    return jsonify({"message": "Training completed", "training_time": training_time})

@commonBp.route('/recommend')
def recommend():
    if index is None:
        return jsonify({"error": "Model is not trained yet"}), 400

    data = request.get_json()
    query_text = data.get('text')
    top_k = data.get('top_k', 10)

    query_embedding = embed_text(query_text).reshape(1, -1).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    results = [{"id": ids[idx], "text": texts[idx], "distance": float(distances[0][i])} for i, idx in enumerate(indices[0])]
    return jsonify(results)
