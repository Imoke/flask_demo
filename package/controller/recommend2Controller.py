from flask import Flask, request, jsonify
from package.base.app import webapp, commonBp
from package.services.rcdServices import RcdService
import time
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import os


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


app = Flask(__name__)
modelsDir = os.path.abspath(os.path.join(__file__, '../../../models'))
## miniLM = os.path.join(modelsDir, 'bert-base-chinese')
miniLM = os.path.join(modelsDir, 'bert-base-chinese')
tokenizer = AutoTokenizer.from_pretrained(miniLM)
model = AutoModel.from_pretrained(miniLM)

# 训练数据存储
corpus = []
corpus_ids = []
corpus_embeddings = []

def compute_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def train_model(train_data_path):
    global corpus, corpus_ids, corpus_embeddings
    corpus = []
    corpus_ids = []

    with open(train_data_path, 'r', encoding='utf-8') as f:
        for line in f:
            id, text = line.strip().split(' ', 1)
            corpus_ids.append(id)
            corpus.append(text)

    corpus_embeddings = np.array([compute_embedding(text) for text in corpus])

@commonBp.route("/train")
def train():
    start_time = time.time()
    data = request.get_json()
    train_data_path = data['train_data_path']
    train_model(train_data_path)
    end_time = time.time()
    return jsonify({'message': 'Training completed', 'time_taken': end_time - start_time})



@commonBp.route('/recommend')
def recommend():
    data = request.get_json()
    query = data['query']
    query_embedding = compute_embedding(query)
    recommendations = []
    # 计算余弦相似度
    scores = np.dot(corpus_embeddings, query_embedding) / (np.linalg.norm(corpus_embeddings, axis=1) * np.linalg.norm(query_embedding))
    top_k_indices = np.argsort(scores)[-10:][::-1]

    for i in top_k_indices:
        score = scores[i]
        if RcdService.detect_antonyms(query, corpus[i]):
            score *= 0.5  # 如果检测到反义词，将得分降低一半
        recommendations.append({
            'id': corpus_ids[i],
            'text': corpus[i],
            'score': int(score * 100)  # 转换为1-100的得分
        })

    return jsonify({'recommendations': recommendations})
