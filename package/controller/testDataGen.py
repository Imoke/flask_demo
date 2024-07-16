import random
import os

# 生成单个故障现象
def generate_fault():
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
    num_words = random.randint(2, 4)  # 选择 2 到 4 个词语组合成一个故障现象
    phenomenon = "".join(random.choices(words, k=num_words)) + "".join(random.choices(fault_phrases, k=1))
    return phenomenon[:40]  # 保证不超过 30 个字

# 生成500条故障现象
faults = [generate_fault() for _ in range(5000)]

# 将故障现象写入文件
output_file = 'fault_phenomena.txt'
i = 1
with open(output_file, 'w', encoding='utf-8') as f:
    for fault in faults:
        f.write(str(i) + " " + fault + '\n')
        i = i + 1

print(f"生成的故障现象数据已写入 {output_file}")
