#-*-coding:utf-8-*-

class Student1(object):
    pass


def test_student1():
    s1 = Student1()
    s1.name = 'KeBi'

    print(vars(s1))

class Student2(object):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getage(self):
        return self.__age

def test_student2():
    s2 = Student2('ppd',11)
    print(vars(s2))
    print('name: {}, age: {}'.format(s2.getName(),s2.getage()))


class Student3(object):
    __slots__ = ('name','age','sex')
    pass

def test_student3():
    s3 = Student3()
    s3.name = 'ppd'
    s3.age = 11
    s3.sex = 1

    print('name : {}, age : {}, sex : {}'.format(s3.name,s3.age,s3.sex))

    # s3.score = 5
    # print('score : {}'.format(s3.score))

if __name__ == '__main__':
    test_student3()
    # test_student2()
    # test_student1()