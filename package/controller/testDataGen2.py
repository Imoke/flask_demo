import random
import nltk
from nltk.corpus import wordnet
import os

# 下载所需的 nltk 数据
nltk.download('wordnet')
nltk.download('omw-1.4')

# 原始词汇列表和故障现象短语
words = [
    "温度", "压力", "流量", "振动", "漏水", "电机", "泵", "管道", "变压器", "锅炉",
    "风机", "燃烧器", "蒸汽", "冷却", "疏水阀", "加热器", "润滑油", "控制系统",
    "排烟", "备用电源", "点火", "供给", "电气", "冷凝器", "叶片", "密封", "水位",
    "电缆", "保护装置", "绝缘"
]
fault_phrases = [
    "异常升高", "不足", "剧烈", "过低", "超限", "泄漏", "堵塞", "不稳定", "过载报警",
    "波动", "破裂", "失效", "停机", "误动作", "压力不足", "振动增大", "启动失败",
    "磨损", "读数异常", "腐蚀", "点火失败", "效率降低", "温度高", "出力不足", "频繁启动"
]

# 查找同义词
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word, lang='cmn'):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# 生成单个故障现象
def generate_fault():
    num_words = random.randint(2, 4)  # 选择 2 到 4 个词语组合成一个故障现象
    chosen_words = random.choices(words, k=num_words)
    chosen_phrase = random.choice(fault_phrases)

    # 引入同义词
    if random.random() < 0.3:  # 30% 几率替换一个词语为同义词
        word_to_replace = random.choice(chosen_words)
        synonyms = get_synonyms(word_to_replace)
        if synonyms:
            chosen_words[chosen_words.index(word_to_replace)] = random.choice(synonyms)

    # 引入双重否定
    if random.random() < 0.3:  # 30% 几率引入双重否定
        chosen_phrase = "不" + chosen_phrase.replace("不", "")

    phenomenon = "".join(chosen_words) + chosen_phrase
    return phenomenon

# 生成1000条故障现象
faults = [generate_fault() for _ in range(1000)]

# 将故障现象写入文件
i = 1
output_file = 'fault_phenomena_1000.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for fault in faults:
        f.write(str(i) + " " + fault + '\n')
        i = i + 1

print(f"生成的故障现象数据已写入 {output_file}")
