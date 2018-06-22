#-*-coding:utf-8-*-

def slice_test():
    list_base = ['Michael','Sarah','Tracy','Bob','Jack','KeBi']
    list_data_01 = list_base[1:3]
    print(list_data_01)    # ['Sarah', 'Tracy']


def sorted_test():
    list_data = [36, 5, 12, 9, 21]
    print(sorted(list_data))

def test():
    dict_base = {'66':'AB66','99':'RR90'}
    for i,value in enumerate(['A','B','C','D','E','F']):
        dict_base[i] = value
    print(dict_base)

from collections import Iterable

def iteration_test():
    int_base = 78787899
    str_base = 'ABCD1234'
    list_base = ['123','B',777,'D','E','F']
    tuple_base = ('A','B','C',123,'D','6666')
    dict_base = {'01':'AA','02':'BB','03':'CC'}

    if isinstance(int_base,Iterable):
        for i in int_base:
            print(i)
    if isinstance(str_base,Iterable):
        for i in str_base:
            print(i)
    if isinstance(list_base,Iterable):
        for i in list_base:
            print(i)
    if isinstance(tuple_base,Iterable):
        for i in tuple_base:
            print(i)
    if isinstance(dict_base,Iterable):
        for i,value in dict_base:
            print(i,value)

def range_test():
    # 1++2+3+4+5+6+7+8+9
    sum = 0
    for i in range(0,10,1):
        sum = sum + i
    print(sum)

    # 1*1 + 2*2 + 3*3 + ... + 9*9
    product_sum = 0
    for i in range(0,10,1):
        product_sum = product_sum + i*i
    print(product_sum)

    str_base = 'XYZ'
    print(str_base[1])
    print('----------------------------')

    for i in range(len(str_base)):
        print(str_base[i])

def f(x):
    return x*x

def map_test():
    list_base = [1,2,3,4,5,6,7,8,9]
    map_data = map(f,list_base)
    print(map_data)

def add(x,y):
    return x + y

def reduce_test():
    list_base = [1,3,5,7,9]
    sum = reduce(add,list_base)
    print(sum)


if __name__ == '__main__':
    print(reduce_test.__name__)
    # reduce_test()
    # map_test()
    # range_test()
    # iteration_test()
    # test()
    # slice_test()
    # sorted_test()