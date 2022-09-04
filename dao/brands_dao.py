# -*- coding: utf-8 -*-
import sqlite3

class BrandsDAO(object):
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name

    def get_brands_code_list(self):
        conn = sqlite3.connect(self.db_file_name)
        with conn:
            code_list = []
            result_list = conn.execute('SELECT code from brands').fetchall()
            for result in result_list:
                code_list.append(result[0])
            return code_list
