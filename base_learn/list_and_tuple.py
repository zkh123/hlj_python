

'''
list
list is a type of data

[]

append()
insert()

pop()
remove()

list[i]

len(list)
'''
def list_test():
    list_base = ['a',123,'3df23d','123']
    print('list_base {}'.format(list_base))

    '''
    add operate    
    '''
    list_base.append(['wwwww','666666',123456])
    print('list_base {}'.format(list_base))

    list_base.insert(1,'kebi')
    print('list_base {}'.format(list_base))

    '''
    delete operate
    '''
    list_base.pop(1)
    print('list_base {}'.format(list_base))

    list_base.remove('a')
    print('list_base {}'.format(list_base))


    for param in list_base:
        print('------------- {}'.format(param))
        if param == 123:
            print('YYYYYYY')
        elif param == '123':
            print('XXXXXXX')
        else:
            print('ZZZZZZZZ')

    print('list_base[1] {}'.format(list_base[3]))
    print('list_base len {}'.format(len(list_base)))

    list_base.pop()
    print('list_base {}'.format(list_base))
    list_base.pop(len(list_base)-2)
    print('list_base {}'.format(list_base))

    list_data = list_base
    print('list_data {}'.format(list_data))

    list_data[0] = '666666666666'
    print('list_data {}'.format(list_data))

    '''
    string <--------> list
    '''
    a = '123abc666'
    list_data_1 = list(a)
    print('list_data_1 {}'.format(list_data_1))  # ['1', '2', '3', 'a', 'b', 'c', '6', '6', '6']

    list_data_2 = ['1', '2', '3', 'a', 'b', 'c', '6', '6', '6']
    str_convert = ''.join(list_data_2)
    print('str_convert {}'.format(str_convert))   # 123abc666

    list_base.append((1,2,3,4,'kebi'))
    print('list_base {}'.format(list_base))
    print('list_base[2][4] {}'.format(list_base[2][4]))
    list_base.append('123')
    print(list_base)

def tuple_test():
    tuple_base = (1,2,3,'4','a',123)
    print('tuple_base {}'.format(tuple_base))

    print(tuple_base[0])
  # tuple_base[1] = '666666666666'    ---- fail can not change element
   # print('tuple_base {}'.format(tuple_base))

    tuple_data_1 = ('aaa',1234,'666',['kebi','jmouss',789])
    # t = ('a', 'b', ['A', 'B'])
    print(tuple_data_1[3][0])

    list_data = list(tuple_data_1)
    print('tuple_data_1 type {},  list_data type {} ,list_data {}'.format(type(tuple_data_1),type(list_data),list_data))

    list_data[0] = 'bbb'
    print(list_data)

    str_convert = ''.join(tuple_base)
    print(str_convert)

if __name__ == '__main__':
    # tuple_test()
    list_test()