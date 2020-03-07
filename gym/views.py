from rest_framework import viewsets
from rest_framework import permissions
from . import models
from . import serializers

class MemberViewset(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [permissions.IsAuthenticated]