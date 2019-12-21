# -*- coding: utf-8 -*-

# ------------------------------
# @Time    : 2019/12/18
# @Author  : gao
# @File    : save_get_indicator.py
# @Project : AmazingQuant 
# ------------------------------
import os

import pandas as pd
from mongoengine.context_managers import switch_collection

from AmazingQuant.data_center.mongo_connection import MongoConnect
from AmazingQuant.utils.performance_test import Timer
from AmazingQuant.data_center.database_field.field_indicator import Indicator
from AmazingQuant.constant import DatabaseName
from AmazingQuant.data_center.get_data.get_calendar import GetCalendar


class SaveGetIndicator(object):
    def __init__(self):
        pass

    def save_indicator(self, indicator_name, input_data):
        path_save = '../../../../data/indicator/'
        if not os.path.exists(path_save):
            os.mkdir(path_save)
        input_data.to_hdf(path_save + indicator_name + '.h5', key=indicator_name, mode='w')

    def get_indicator(self, indicator_name):
        path_save = '../../../../data/indicator/' + indicator_name + '.h5'
        if not os.path.exists(path_save):
            return None
        return pd.read_hdf(path_save)


if __name__ == '__main__':
    with Timer(True):
        indicator_data = SaveGetIndicator().get_indicator('close')

