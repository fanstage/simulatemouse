from django.db import models

# Create your models here.


class Goods(models.Model):
    gid = models.IntegerField(max_length=25)
    gname = models.CharField(max_length=25)
    gprice = models.IntegerField(max_length=25)


Goods.objects.create(gid="1", gname='英文小王子', gprice='99')