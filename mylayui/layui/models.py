from django.db import models

# Create your models here.


class Cuetomer(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()

    def __str__(self):
        return "<%s %s>"%(self.name,self.age)
    class Meta:
        verbose_name_plural = '客户表'
        verbose_name='客户表'







