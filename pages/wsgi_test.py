#-*-coding:utf-8-*-


'''
    environ：一个包含所有HTTP请求信息的dict对象；
    start_response：一个发送HTTP响应的函数。
'''
def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])

    method=environ['REQUEST_METHOD']
    path=environ['PATH_INFO']

    print('method : {}, path : {}'.format(method,path))

    return '<h1>Hello,Web!</h1>'
    # return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')