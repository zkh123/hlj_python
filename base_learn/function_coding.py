#-*-coding:utf-8-*-

def log(func):
    def wrapper(*args,**kw):
        print('call {}'.format(func.__name__))
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-6-22')


try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5
import sys


def stringAndJson_test():
    print(sys.path)


if __name__ == '__main__':
    stringAndJson_test()
    # now()