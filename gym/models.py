# import uuid
from django.db import models

from datetime import datetime
from datetime import timedelta
# Create your models here.


class Member(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False)
    name = models.CharField(max_length=200)
    adm_no = models.AutoField('Admission no',primary_key=True)
    age = models.IntegerField('Age of the person')
    weight = models.FloatField('weight of the person')
    height = models.FloatField('height of the person')
    duration = models.IntegerField('subscription duration', null= False)

    phone = models.IntegerField('phone no', max_length=10)
    date_joined = models.DateField(
        ("Date joined"), auto_now=False, auto_now_add=False)
    exp_date = models.DateField(
        ("Date renewed"), auto_now=False, auto_now_add=False,)
    address = models.CharField(max_length=500)
    payment_status = models.BooleanField('subscribed or not', default=True)
    photo = models.FileField(blank=False, null=True)
    
    def __uuid__(self):
        return self.adm_no


# class PaymentRecords(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)
#     renew_date = models.DateField(
#         ("Date renewed"), auto_now=False, auto_now_add=False)
#     duration = models.IntegerField('subscription duration')

    # def exp(self):
    #     months = self.duration*30
    #     return self.renew_date + timedelta(days= months)

    # def exp(self):
    #     return self.annotate(
    #         exp_date=models.Case(
    #             models.When(
    #                 borrowed__when__lte=pendulum.now().subtract(months=2),
    #                 then=True),
    #             output_field=models.DateField()
    #         )
    #     )
