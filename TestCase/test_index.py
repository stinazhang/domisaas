#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from common.readconfig import conf
from utils.log import log
import yaml
from ddt import ddt, data, unpack, file_data
import time
from selenium.webdriver.support.ui import WebDriverWait
from common.connect_db import operation_mysql

class TestIndex:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(2)

    def test_switch_device(self, drivers):
        '''切换到设备管理页'''
        index = Index(drivers)
        index.switch_device()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '设备列表'
        index.swtich_to_default()

    def test_switch_message(self, drivers):
        '''切换到消息列表页'''
        index = Index(drivers)
        index.switch_message()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '消息列表'
        index.swtich_to_default()

    def test_switch_feedback(self, drivers):
        '''切换到用户反馈页'''
        index = Index(drivers)
        index.switch_feedback()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '反馈信息列表'
        index.swtich_to_default()

    def test_switch_product(self, drivers):
        '''切换到产品管理页'''
        index = Index(drivers)
        index.switch_product()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '产品列表'
        index.swtich_to_default()

    def test_switch_ability(self, drivers):
        '''切换到产品能力管理页'''
        index = Index(drivers)
        index.switch_product_ability()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '产品能力列表'
        index.swtich_to_default()

    def test_switch_firm(self, drivers):
        '''切换到厂商管理页'''
        index = Index(drivers)
        index.switch_firm()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '厂商列表'
        index.swtich_to_default()

    def test_switch_agency(self, drivers):
        '''切换到代理商页'''
        index = Index(drivers)
        index.switch_agency()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '子账户列表'
        index.swtich_to_default()

    def test_switch_role(self, drivers):
        '''切换到角色管理页'''
        index = Index(drivers)
        index.switch_role()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '角色列表'
        index.swtich_to_default()

    def test_switch_permission(self, drivers):
        '''切换到权限管理页'''
        index = Index(drivers)
        index.switch_peimission()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '权限列表'
        index.swtich_to_default()

    def test_switch_account(self, drivers):
        '''切换到用户管理页'''
        index = Index(drivers)
        index.switch_account()
        time.sleep(1)
        index.switch_to_iframe()
        title_name = index.ifram_text()
        assert title_name == '账户设置'
        index.swtich_to_default()


# if __name__ == '__main__':
#     pytest.main(['test_index.py'])
