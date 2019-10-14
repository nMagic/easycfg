# -*- coding: utf-8 -*-
import yaml
import json


class ConfigDict(dict):
    def __init__(self, __d={}, **kwargs):
        data = __d if __d else kwargs
        for key in data:
            if type(data[key]) == type(dict()):
                data[key] = ConfigDict(**data[key])
            elif type(data[key]) == type(list()):
                data[key] = ConfigList(data[key])
        super().__init__(data)

    def __getattribute__(self, name):
        return self[name]


class ConfigList(list):
    def __init__(self, __l):
        data = list(__l)
        for i in range(len(data)):
            if type(data[i]) == type(list()):
                data[i] = ConfigList(data[i])
            elif type(data[i]) == type(dict()):
                data[i] = ConfigDict(data[i])
        super().__init__(data)

    def __getitem__(self, key):
        data = super().__getitem__(key)
        if isinstance(data, dict):
            return ConfigDict(data)
        elif isinstance(data, list):
            return ConfigList(data)

    def __getattribute__(self, name):
        result = list()
        for item in self:
            if isinstance(item, dict):
                if name in item:
                    result.append(item[name])
        return ConfigList(result)


def config_load(filename):
    funcs = {
        'yml': yaml.safe_load,
        'yaml': yaml.safe_load,
        'json': json.load,
    }
    with open(filename) as file:
        ext = file.name.split('.')[-1].lower()
        data = funcs[ext](file)
    if isinstance(data, dict):
        return ConfigDict(data)
    elif isinstance(data, list):
        return ConfigList(data)
