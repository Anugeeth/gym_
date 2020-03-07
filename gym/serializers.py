from rest_framework import serializers
from .models import Member
      
class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ('name', 'phone', 'age','address','weight','height','duration','payment_status','date_joined','photo')