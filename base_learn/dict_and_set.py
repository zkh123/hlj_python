#-*-coding:utf-8-*-

def dict_test():
    dict_base = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print('dict_base: {}'.format(dict_base))
    dict_base['kebi'] = 24
    print('dict_base: {}'.format(dict_base))
    print(dict_base.pop('Tracy'))
    print('dict_base: {}'.format(dict_base))
    print(dict_base.get('Bob'))


def set_test():
    list_data = ['aaa',1234,1234]
    s = set(list_data)
    print('list_data type: {}, s type: {}, s: {}'.format(type(list_data),type(s),s))


    s.add('12345678')
    print(s)

    print('aaa' in s)
if __name__ == '__main__':
    set_test()
    # dict_test()