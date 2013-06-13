# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import User, HoroscopeModel
from datetime import date, timedelta, datetime
import random
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
    print 'rd', r_date
    signs = getSigns()
    res = []
    for sign in signs:
        h = getHoroscopeBySignAndDate(sign, r_date)
        if (h):
            res.append(h)
    return res

def parseDateString(r_date):
    res = r_date.replace('.', '-')
    return res

def parseDate(r_date):
    splited = r_date.split('-')
    return date(day=int(splited[0]), month=int(splited[1]), year=int(splited[2]))

def updateUser(exists, user):
    updated = False
    if exists.bdate != user.bdate:
        exists.bdate = user.bdate
        updated = True
        print 'exis1'
    if exists.img_src != user.img_src:
        exists.img_src = user.img_src
        updated = True
        print 'exis2'
    if exists.name != user.name:
        exists.name = user.name
        updated = True
        print 'exis3'
    if str(exists.sex) != str(user.sex):
        exists.sex = user.sex
        updated = True
        print 'exis4'

    if updated:
        exists.save()
        print 'updated', exists.uid

def handle_get_request(request):
    if request:
        h = getHoroscopesByDate(yesterday())
        random.shuffle(h)
        c = {'horoscopes': h, 'date': yesterday()}

        if request.method == 'GET':
            c.update(csrf(request))
            return render_to_response('vk_login/index.html', c)
    else:
        return HttpResponse('Failed - no request')

def login(request):
    if request:
        if request.method == 'POST':
            if 'uid' in request.POST and 'name' in request.POST \
                and 'img_src' in request.POST and 'sex' in request.POST and 'bdate' in request.POST:

                exists = User.objects.filter(uid=request.POST['uid'])
                user = User(uid=request.POST['uid'], name=request.POST['name'], sex=str(request.POST['sex']),
                         img_src=request.POST['img_src'], bdate=parseDateString(request.POST['bdate']))

                if exists:
                    print 'exists', exists[0].uid
                    updateUser(exists[0], user)
                else:
                    user.save()
                    print 'saved', user.uid

                s = getSignByDate(parseDate(user.bdate))
                print s

                return HttpResponse('success_info')

    return HttpResponse('error')

def getHoroscopeById(r_id):
    return HoroscopeModel.objects.get(id=r_id)

def getUserSignById(user_id):
    user = User.objects.get(uid=user_id)
    sign = getSignByDate(parseDate(user.bdate))
    return sign

def sign(request):
    if request:
        if request.method == 'POST':
            print request.POST.keys()
            if 'uid' in request.POST and 'horoscope_id' in request.POST:
                g = 0
                selected_sign = getHoroscopeById(request.POST['horoscope_id']).sign
                user_sign = getUserSignById(request.POST['uid'])
                if selected_sign == user_sign:
                    g = 1
                return HttpResponse(str(g) + ';' + request.POST['horoscope_id'] + ';' + selected_sign)
    return HttpResponse('error')
