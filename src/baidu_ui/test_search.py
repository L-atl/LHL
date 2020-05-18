
#-*- coding:utf-8 -*-
import pytest
import xlrd
from selenium import webdriver
from time import sleep, ctime
import os
import sys
sys.path.append('../')
import  baidu_ui.const as const



class Test_baidu_search():
    def test_search_from_excel(self,excel_dir=const.EXCEL_DIR):

        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        #打开excel
        excel_file= xlrd.open_workbook(excel_dir)
        #获取第一个sheet
        sheet = excel_file.sheet_by_index(0)
        #获取第一列数据，返回列表
        cols=sheet.col_values(0)
        print(cols)
        #遍历列表，拿取数据作为测试输入
        for query in cols:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(query))
            driver.find_element_by_id("su").click()
            sleep(2)

        driver.quit()
    def test_ssss(self):
        #todo .......
        print("111111111111111111111")
        assert   1==1
