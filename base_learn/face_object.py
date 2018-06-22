#-*-coding:utf-8-*-


class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('name : {}, score : {}'.format(self.name,self.score))

def student_test():
    bart = Student('Bart simpson',59)
    print(bart.name)
    lisa = Student('Lisa Simpson',87)
    print(lisa.score)
    bart.print_score()
    lisa.print_score()

class Student2(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('name : {}, score : {}'.format(self.__name,self.__score))

def student2_test():
    bart = Student2('Bart simpson',59)
    # print(bart.__name)
    lisa = Student2('Lisa Simpson',87)
    # print(lisa.score)
    bart.print_score()
    lisa.print_score()

import types

def type_test():
    str_base = 'abc'
    int_base = 123
    list_base = ['abc',123,'hello']
    tuple_base = ('abc',123,'hello')
    dict_base = {'abc':'ABC','2':'123','see':'hello'}
    set_base = {'abc',123,'66666',123}   #  {'abc',123,'66666'}

    print('type of str_base : {}, type of int_base : {}, type of list_base : {}, type of tuple_base : {}, type of dict_base : {}, type of set_base : {}'.
          format(type(str_base),type(int_base),type(list_base),type(tuple_base),type(dict_base),type(set_base)))

    print(type(str_base) == types.StringType)
    print(type(int_base) == types.IntType)
    print(type(list_base) == types.ListType)
    print(type(tuple_base) == types.TupleType)
    print(type(dict_base) == types.DictType)

    print set_base



if __name__ == '__main__':
    type_test()
    # student_test()
    # student2_test()