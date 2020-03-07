from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField('Age of the person')
    weight = models.IntegerField('weight of the person')
    height = models.IntegerField('height of the person')
    phone = models.IntegerField('phone no',max_length=10, primary_key=True)
    date_joined = models.DateField(("Date joined"), auto_now=False, auto_now_add=False)
    address = models.CharField(max_length= 500)
    duration = models.IntegerField('subscription duration')
    payment_status = models.BooleanField('subscribed or not', default=True)
    photo = models.URLField('image url')
