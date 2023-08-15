from django.db import models

# Create your models here.
class Member(models.Model):
    #중복제거 unique=True 유일해야 한다 
    userid = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    wdate = models.DateTimeField()

#python manage.py makemigrations member 
#python manage.py migrate 

