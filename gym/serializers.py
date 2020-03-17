from rest_framework import serializers
from .models import Member,PaymentRecords
      
class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    
    fields = ('id','name', 'phone', 'age','address','weight','height','exp_date','payment_status','date_joined','photo')

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PaymentRecords
    fields = ('member','renew_date','duration')