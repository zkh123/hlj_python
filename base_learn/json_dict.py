#-*-coding:utf-8-*-

import json

def json_test():
    dict_base = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

    json_data = json.dumps(dict_base)

    python_object = json.loads(json_data)
    print('dict_base type : {} ,json_data type : {}, python_object : {}'.format(type(dict_base),type(json_data),type(python_object)))

    print('dict_base type : {} ,json_data type : {}, python_object : {}'.format(dict_base,json_data,python_object))

if __name__ == '__main__':
    json_test()