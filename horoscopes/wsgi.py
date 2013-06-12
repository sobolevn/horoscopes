"""
WSGI config for horoscopes project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "horoscopes.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from HoroscopeView.engine.parser import getAllHoroscopes
from HoroscopeView.models import HoroscopeModel

def missing(r_date, r_sign):
    res = HoroscopeModel.objects.filter(sign=r_sign, date=r_date)
    if res.count() == 0:
        return True
    else:
        return False

def prepareHoroscopes():
    print 'starting to parse'
    horoscopes = getAllHoroscopes()
    for key in horoscopes.keys():
        for horoscope in horoscopes[key]:
            print horoscope
            if missing(horoscope.date, horoscope.sign):
                horoscope.getModel().save()
                print 'saved'
            else:
                print 'already existed'
    print 'finished'

if __name__ == 'horoscopes.wsgi':
    prepareHoroscopes()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
