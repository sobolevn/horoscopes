# -*- coding: utf8 -*-
__author__ = 'sobolev'

import feedparser
import re
from datetime import date, datetime
from horoscope import Horoscope
from statics import getSigns
from time import mktime

_base_url = 'http://horo.tochka.net/rss/horoscopes/day/'

_date_pattern = re.compile(
    r'(\d{,2}).(\d{,2}).(\d{4})')

#datetime.datetime(Mon Feb 15 2010, "%a %b %d %Y").strftime("%d/%m/%Y")

def parseDate(r_date):
    parsed = r_date.replace(' +0300', '')
    #print type(datetime.strptime(parsed, '%a, %d %b %Y %H:%M:%S').strftime('%d-%m-%Y'))
    #print datetime.strptime('Mon, 17 Jun 2013 00:00:00', '%a, %d %b %Y %H:%M:%S').strftime('%d-%m-%Y')
    splited = datetime.strptime(parsed, '%a, %d %b %Y %H:%M:%S').strftime('%d-%m-%Y').split('-')
    return date(int(splited[2]), int(splited[1]), int(splited[0]))

#r_date = 'Mon, 17 Jun 2013 00:00:00 +0300'
#print 'res', parseDate(r_date), type(parseDate(r_date))

def dateHandler(aDateString):
    month, day, year, hour, minute, second = \
        _date_pattern.search(aDateString).groups()
    return (int(year), int(month), int(day), \
        int(hour), int(minute), int(second), 0, 0, 0)

feedparser.registerDateHandler(dateHandler)

def getDate(parsed_date):
    print 'parsed', datetime.fromtimestamp(mktime(parsed_date))
    return date(parsed_date.tm_year, parsed_date.tm_mon, parsed_date.tm_mday)

def removeSignsText(text):

    return text

def getHoroscopesForSign(sign):
    parsed = feedparser.parse(_base_url + sign)
    horoscope_list = []
    #print parsed.items()
    for i in parsed.entries:
        date = parseDate(i.published)
        text = i.fulltext.replace('...', '')
        horoscope_list.append(Horoscope(text, sign, date))
    return horoscope_list

def getHoroscopeForSignAndDate(sign, date):
    parsed = feedparser.parse(_base_url + sign)
    for i in parsed.entries:
        r_date = getDate(i.published_parsed)
        if r_date == date:
            return Horoscope(i.fulltext, sign, date)


def getAllHoroscopes():
    signs = getSigns()
    all_horoscopes = {}
    for sign in signs:
        all_horoscopes.update({sign: getHoroscopesForSign(sign)})
    return all_horoscopes

#print getHoroscopeForSignAndDate('taurus', date.today())