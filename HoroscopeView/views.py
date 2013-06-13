# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import User, HoroscopeModel
from datetime import date, timedelta
from engine.horoscope import Horoscope, fromModel
from engine.statics import *

def yesterday():
    delta = timedelta(days=1)
    today = date.today()
    return today - delta

def today():
    return date.today()

def getHoroscopeBySignAndDate(r_sign, r_date):
    res = HoroscopeModel.objects.filter(sign=r_sign, date=r_date)
    if res.count() == 1:
        return fromModel(res[0])

def getHoroscopesByDate(r_date):
    signs = getSigns()
    res = []
    for sign in signs:
        h = getHoroscopeBySignAndDate(sign, r_date)
        if (h):
            res.append(h)
    #print len(res)
    return res

def login(request):
    """

    :param request:
    :return:
    """
    if request:
        h = getHoroscopesByDate(yesterday())
        c = {'horoscopes': h, 'date': yesterday()}

        if request.method == 'GET':
            c.update(csrf(request))
            return render_to_response('vk_login/login.html', c)

        else:
            if 'uid' in request.POST and 'name' in request.POST \
                and 'img_src' in request.POST and 'sex' in request.POST and 'bdate' in request.POST:
                c.update({'login_val': True})
                c.update(csrf(request))
                print 'suc'
                check = User.objects.filter(uid=request.POST['uid'])
                if not check:
                    u = User(uid=request.POST['uid'], name=request.POST['name'], sex=request.POST['sex'],
                         img_src=request.POST['img_src'], bdate=request.POST['bdate'])
                    u.save()
                    print 'saved' + u.uid

                return HttpResponse('success') # render_to_response('vk_login/login.html', c)
            else:
                return HttpResponse('error')

    else:
        return HttpResponse('Failed - no request')