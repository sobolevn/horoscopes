# Create your views here.
from django.template import Template
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import User

def login(request):
    """

    :param request:
    :return:
    """
    #t = get_template('page1.html')
    if request:
        if request.method == 'GET':
            c = {}
            c.update(csrf(request))
            return render_to_response('durovat/login.html', c)

        else:
            print 'post'
            if 'uid' in request.POST and 'name' in request.POST \
                and 'img_src' in request.POST and 'sex' in request.POST and 'bdate' in request.POST:
                c = {'login_val': True}
                c.update(csrf(request))
                check = User.objects.filter(uid=request.POST['uid'])
                if not check:
                    u = User(uid=request.POST['uid'], name=request.POST['name'], sex=request.POST['sex'],
                         img_src=request.POST['img_src'], bdate=request.POST['bdate'])
                    u.save()
                    print 'saved' + u.uid

                return render_to_response('durovat/login.html', c)
            else:
                return HttpResponse('error')

    else:
        return HttpResponse('Failed - no request')