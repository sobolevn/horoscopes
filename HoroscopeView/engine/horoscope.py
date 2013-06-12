# -*- coding: utf8 -*-
__author__ = 'sobolev'

#from HoroscopeView.models import HoroscopeModel
from statics import getSigns


class Horoscope:

    def __init__(self, description, sign, date):
        """
        Class representing a horoscope object
        :param description:
        :param sign:
        :param date:
        """
        self.description = description
        self.sign = sign
        self.date = date

    def getModel(self):
        print 'd'
        #return HoroscopeModel(description=self.description, sign=self.sign, start_date=self.start_date)

    def getDueDate(self):
        sign = getSigns()
        print sign.taurus
