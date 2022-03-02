# -*- coding: utf-8 -*-
import yaml
import os
import sys
import copy


def getConfig(filePath):
    # 打开yaml文件
    if os.path.exists(filePath) is False:
        return {}

    file = open(filePath, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def deepMerge(target, src):
    for k, v in src.items():
        if type(v) == list:
            target[k] = copy.deepcopy(v)
        elif type(v) == dict:
            if not k in target:
                target[k] = copy.deepcopy(v)
            else:
                deepMerge(target[k], v)
        elif type(v) == set:
            if not k in target:
                target[k] = v.copy()
            else:
                target[k].update(v.copy())
        else:
            target[k] = copy.copy(v)
    return target


configDir = os.path.abspath(os.path.join(__file__, '../../../../config'))

devConfigFile = os.path.join(configDir, 'dev.yaml')
prodConfigFile = os.path.join(configDir, 'prod.yaml')
localConfigFile = os.path.join(configDir, 'local.yaml')

localConfig = getConfig(localConfigFile)
devConfig = getConfig(devConfigFile)
prodConfig = getConfig(prodConfigFile)


def getMergedConfig():
    if os.environ.get('FLASK_ENV') == 'development':
        return deepMerge(devConfig, localConfig)
    return prodConfig


config = getMergedConfig()

print(config)
