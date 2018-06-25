#-*-coding:utf-8-*-

import os

def test():
    print('Process {} start...'.format(os.getpid()))
    pid = os.fork()
    if pid==0:
        print('i am child process {} and my parent is {}'.format(os.getpid(),os.getppid()))
    else:
        print('i {} just created a child process {}'.format(os.getpid(),pid))

    print(pid)



if __name__ == '__main__':
    test()