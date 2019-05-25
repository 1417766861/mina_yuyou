#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 21:48
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser,UserManager

class User_Manager(UserManager):
    def _create_user(self, email,username, password, **extra_fields):
        if not email:
            raise ValueError("必须要传递email")
        if not password:
            raise ValueError("必须要传递密码")
        user = self.model(username=username,phone=email,**extra_fields)
        user.set_password(password)
        user.save()


    def create_user(self,email,username,password, **extra_fields):
        extra_fields['is_superuser'] = False
        return self._create_user(email,username,password,**extra_fields)

    def create_superuser(self,email,username,password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(email,username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("邮箱",max_length=40,null=False,unique=True)
    address = models.CharField("地址",max_length=40)
    username = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

