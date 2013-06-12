# -*- coding: utf8 -*-
__author__ = 'sobolev'

from datetime import date

def getSigns():
    """
    :return:
    """
    sign = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
            'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    return sign

def getRussianSigns():
    """
    :return:
    """
    sign = ['овен', 'телец', 'близнецы', 'рак', 'лев',
            'дева', 'весы', 'скорпион', 'стрелец', 'козерог',
            'водолей', 'рыбы']
    return sign

def swap(sign):
    signs = getSigns()
    rus = getRussianSigns()
    if (signs.count(sign)):
        return rus[signs.count(sign)]
    if (rus.count(sign)):
        return signs[rus.count(sign)]
    return None


def getSignBorders():
    borders = [(80, 110), (111, 140), (141, 172), (173, 203), (204, 235), (236, 266), (267, 295),
                (296, 326), (327, 355), (356, 20), (21, 50), (51, 79)]
    return borders

def getSignsWithBorders():
    borders = getSignBorders()
    signs = getSigns()
    res = {}
    for i in range(0, len(signs)):
        res.update({signs[i]: borders[i]})
    return res


def getSignByDate(required_date):
    dict = getSignsWithBorders()
    days_passed = required_date.timetuple().tm_yday
    for key in dict.keys():
        d1, d2 = dict[key]
        if(d1 < d2):
            if(days_passed >= d1 and days_passed <= d2):
                return key
        else:
            if((days_passed <= d2 and days_passed >= 1)
               or (days_passed >= d1 and days_passed <= 365)):
                return key

    #print d1.strftime("%d/%m/%Y")


#print swap('taurus')
#print swap('Телец')
#print swap('tauru')
#print swap('телец')
#print swap('теле')
#print getSignByDate(date(2013, 5, 8))
#print getSignByDate(date(2013, 12, 28))
#print getSignByDate(date(2013, 1, 3))
#print getSignByDate(date(2013, 12, 21))
#print getSignByDate(date(2013, 12, 22))
#print getSignByDate(date(2013, 1, 1))
#print getSignByDate(date(2013, 2, 4))