import os
import re

class RcdService():
    config_dir = os.path.abspath(os.path.join(__file__, '../../../config'))
    global antonyms_config
    antonyms_config = os.path.join(config_dir, 'antonyms.txt')

    @classmethod
    def load_antonyms(cls, file_path):
        antonyms = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word1, word2 = line.strip().split(':')
                antonyms[word1] = word2
                antonyms[word2] = word1  # 确保反向关系也包含在字典中
        return antonyms


    @classmethod
    def detect_antonyms(cls, text1, text2):
        antonyms_dict = RcdService.load_antonyms(antonyms_config)
        words1 = set(re.findall(r'\b\w+\b', text1))
        words2 = set(re.findall(r'\b\w+\b', text2))
        for word1 in words1:
            if word1 in antonyms_dict and antonyms_dict[word1] in words2:
                return True
        return False
