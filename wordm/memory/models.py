from django.db import models
from io import  BytesIO
from PIL import Image
from django.core.files import File


# Create your models here.
class Userinfo(models.Model):
    userid = models.IntegerField(max_length=20, null=False)
    userphone = models.CharField(max_length=11)
    nickname = models.CharField(max_length=25)
    class Meta:
        ordering = ('userid',)

    def __str__(self):
        return self.userid





