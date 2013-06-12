# -*- coding: utf8 -*-
__author__ = 'sobolev'

import feedparser
import re
from datetime import date
from horoscope import Horoscope
from statics import getSigns

_base_url = 'http://horo.tochka.net/rss/horoscopes/day/'

_date_pattern = re.compile(
    r'(\d{,2}).(\d{,2}).(\d{4})')

def dateHandler(aDateString):
    month, day, year, hour, minute, second = \
        _date_pattern.search(aDateString).groups()
    return (int(year), int(month), int(day), \
        int(hour), int(minute), int(second), 0, 0, 0)

feedparser.registerDateHandler(dateHandler)

def getDate(parsed_date):
    return date(parsed_date.tm_year, parsed_date.tm_mon, parsed_date.tm_mday)

def getHoroscopesForSign(sign):
    parsed = feedparser.parse(_base_url + sign)
    horoscope_list = []
    for i in parsed.entries:
        date = getDate(i.published_parsed)
        horoscope_list.append(Horoscope(i.fulltext, sign, date))
    return horoscope_list

def getHoroscopeForSignAndDate(sign, date):
    parsed = feedparser.parse(_base_url + sign)
    for i in parsed.entries:
        r_date = getDate(i.published_parsed)
        print 'eq', r_date, date, (r_date == date)
        if r_date == date:
            return Horoscope(i.fulltext, sign, date)


def getAllHoroscopes():
    signs = getSigns()
    all_horoscopes = {}
    for sign in signs:
        all_horoscopes.update({sign: getHoroscopesForSign(sign)})
    return all_horoscopes

#print getHoroscopeForSignAndDate('taurus', date.today())