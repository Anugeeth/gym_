from rest_framework import viewsets
from rest_framework import permissions, status

# for search
from rest_framework import filters
# for image upload
from rest_framework.response import Response

from rest_framework.parsers import FileUploadParser

from . import models
from . import serializers


class MemberViewset(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self,request , *args, **kwargs)
    #     queryset = queryset.

# image upload
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = serializers.MemberSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# search
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'payment_status']
