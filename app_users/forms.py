from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )
        labels = {
            "username": ("ชื่อผู้ใช้"),
            "email": ("ที่อยู่อีเมล (ไม่บังคับ)"),
            "password1": ("รหัสผ่าน"),
            "password2": ("ยืนยันรหัสผ่าน"),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": ("ชื่อ"),
            "last_name": ("นามสกุล"),
            "email": ("ที่อยู่อีเมล"),
        }