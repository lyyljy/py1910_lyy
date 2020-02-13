# -*- coding: utf-8 -*-
# @File    : forms.py
# 描述     ：
# @Time    : 2020/2/12
# @Author  : 
# @QQ      :


import re

from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

def check_password(value):
    if re.match(r'\d*$', value):
        raise ValidationError('密码不能是纯数字')


class RegisterForm(forms.Form):
    # 应该和数据库表中的字段名一致
    username = forms.CharField(label='姓名',required=True,error_messages={
        'required':'用户名必须输入'
    })
    password = forms.CharField(min_length=3,required=True,validators=[check_password],
                                error_messages={'min_length':'长度不能少于3位',
                                                'required':'密码必须输入'
                                                })
    confirm = forms.CharField(min_length=3,required=True,validators=[check_password],
                                error_messages={'min_length':'长度不能少于3位',
                                                'required':'密码必须输入'
                                                })
    phone = forms.CharField(min_length=11,max_length=11,error_messages={
        'max_length':'手机号必须是11位',
        'min_length':'手机号必须是11位',
    })

    #验证单个字段
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8[0-9]|9[0-9])\d{8}$',phone):
            raise ValidationError("手机号格式不正确")
        else:
            return phone

    # 全局验证方法（涉及多个字段）
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password != confirm:
            raise ValidationError({'confirm':['两次密码不一致']})
        else:
            return self.cleaned_data


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={
        'required':'用户名必须输入'
    })
    password = forms.CharField()
    captcha = CaptchaField()  # 验证码字段



