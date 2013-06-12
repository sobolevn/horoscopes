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

def getHoroscopesForSign(sign):
    parsed = feedparser.parse(_base_url + sign)
    horoscope_list = []
    for i in parsed.entries:
        date = str(i.published_parsed.tm_mday) + '.' + str(i.published_parsed.tm_mon) + '.' + str(i.published_parsed.tm_year)
        horoscope_list.append(Horoscope(i.fulltext, sign, date))
    return horoscope_list

def getHoroscopesForSignAndDate(sign, date):
    parsed = feedparser.parse(_base_url + sign)
    horoscope_list = []
    for i in parsed.entries:
        date = str(i.published_parsed.tm_mday) + '.' + str(i.published_parsed.tm_mon) + '.' + str(i.published_parsed.tm_year)
        horoscope_list.append(Horoscope(i.fulltext, sign, date))
    return horoscope_list


def getAllHoroscopes():
    signs = getSigns()
    all_horoscopes = {}
    for sign in signs:
        all_horoscopes.update({sign: getHoroscopesForSign(sign)})
    return all_horoscopes

