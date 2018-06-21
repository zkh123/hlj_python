
from django.http import HttpResponse

import logging

def ping(request):
    logging.info('---------------start--------------')
    print('***********************start***************')
    return HttpResponse('OK')