from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




# For costumer user 

USER_TYPE = (
    ('1','super_user'),
    ('2','teacher'),
    ('3','student')
)
class user_type(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    type = models.CharField(max_length=200,choices=USER_TYPE)
    
class HtmlFormModel(models.Model):
    table_name = models.CharField(max_length=100,unique=True,default="")
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default='')
    html = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.table_name

    



    

