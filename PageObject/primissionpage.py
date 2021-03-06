#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

permission = Element('permission')
class PermissionPage(WebPage):
    def click_add(self):
        """点击添加权限"""
        self.is_click(permission.增加)

    def click_edit(self):
        """点击修改权限"""
        self.is_click(permission.修改)

    def click_del(self):
        """点击删除权限"""
        self.is_click(permission.删除)

    def input_permission_name(self, content):
        """输入权限名称"""
        self.input_text(permission.名称输入框, content)

    def input_permission_remark(self, content):
        """输入权限备注"""
        self.input_text(permission.备注输入框, content)

    def input_permission_code(self, content):
        """输入权限编码"""
        self.input_text(permission.编码输入框, content)

    def click_last_row(self):
        """选择最后一行"""
        self.is_click(permission.最后一行)

    def click_save(self):
        """保存"""
        self.is_click(permission.保存)

    def click_rollback(self):
        """撤销"""
        self.is_click(permission.撤销)

    def click_confirm(self):
        """确定"""
        self.is_click(permission.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(permission.取消)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)