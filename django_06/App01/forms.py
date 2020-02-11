# -*- coding: utf-8 -*-
# @File    : forms.py
# 描述     ：自定义表单
# @Time    : 2020/2/11
# @Author  : 
# @QQ      :

from django import forms
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from App01.models import User


def check_password(value):
    """
    验证密码是不是纯数字
    :param value: 密码字符串
    :return: 无
    """
    if re.match(r'\d*$', value, re.I):
        raise ValidationError("密码不能是纯数字")

# 注册表单 表单主要是针对html中表单提交的数据进行验证
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',min_length=6,required=True,
                                error_messages={'required':'用户名必须输入','min_length':'用户名长度不能小于6'}
                               )
    password = forms.CharField(min_length=6,max_length=12,
                               required=True,
                               # validators=[check_password],  # 自定义验证函数
                               validators=[RegexValidator(regex=r'\d*$', message='密码不能是纯数字', code='password')],
                               error_messages={'required': '密码必须输入', 'min_length': '密码长度必须为6~12位', 'max_length':'密码长度必须为6~12位'}
                               )
    confirm_password = forms.CharField(min_length=6,
                               required=True,
                               error_messages={'required': '确认密码必须输入', 'min_length': '密码长度必须大于6'}
                               )
    email = forms.EmailField(error_messages={'invalid':'邮箱格式不正确，例如1290784581@qq.com'})
    phone = forms.CharField(required=True,
                            validators=[RegexValidator(regex=r'^1[34578][0-9]{9}$', message="手机号不符合要求，例如15733190269", code='phone')],
                            error_messages={'required':'手机号必须输入'}
                            )
    # 单个字段的验证方法
    # 方法的名称格式：clean_字段名（）
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 查询数据库
        if User.objects.filter(username=username).first():
            raise ValidationError("用户名重复")
        # 必须把正确数据返回
        return username

    # 全局验证， 涉及多个字段
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        # 判断两者是否相等
        if password != confirm_password:
            raise ValidationError({'confirm_password':['两次密码输入不一致']})
        return self.cleaned_data

