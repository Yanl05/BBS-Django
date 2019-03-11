"""
bbs用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError
from blog import models

# 定义要给注册的form类
class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length": "用户名最长16位",
            "required": "用户名不能为空"
        },
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},)
    )
    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True),
        error_messages={
            "min_length": "密码最少6位",
            "required": "密码不能为空"
        },

    )
    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True),
        error_messages={
            "min_length": "确认密码最少6位",
            "required": "确认密码不能为空"
        }
    )
    email = forms.EmailField(
        label="邮箱",
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"}),
        error_messages={
            "invalid": "邮箱格式不正确",
            "required": "邮箱不能为空"
        },
    )


    # 重写email字段的局部钩子
    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exist = models.UserInfo.objects.filter(email=email)
        if is_exist:
            # 表示邮箱已被注册
            self.add_error("email", ValidationError("邮箱已被注册"))
        else:
            return email

    # 定义全局钩子，验证密码与重复密码是否一致
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data

