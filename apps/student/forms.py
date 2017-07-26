# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={'required':'请输入用户'})
    password = forms.CharField(required=True,error_messages={'required':'请输入密码'})

class PwdupdateForm(forms.Form):
    new_password = forms.CharField(required=True,max_length=12,min_length=6,error_messages={'required':'密码不能空','max_length':'密码长度过长','min_length':'密码长度过短'})
    check_password = forms.CharField(required=True, max_length=12, min_length=6,error_messages={'required': '请确认密码','max_length': '密码长度过长','min_length': '密码长度过短'})

class UserinfoForm(forms.Form):
    phone = forms.CharField(required=True,error_messages={'required':'请输入电话'})
    email = forms.CharField(required=True,error_messages={'required':'请输入邮箱'})
