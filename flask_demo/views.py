#-*-coding:utf-8-*-

'''
Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
$ easy_install jinja2

在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。
很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
'''

from flask import Flask,request,render_template

views = Flask(__name__)


@views.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@views.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@views.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)


if __name__ == '__main__':
    views.run()