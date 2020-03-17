from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from . import models, serializers


class MemberViewset(viewsets.ModelViewSet):
    queryset = models.Member.objects.all().order_by('exp_date')
    serializer_class = serializers.MemberSerializer
    # uncomment before auth integration
    # permission_classes = [permissions.IsAuthenticated]
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
    search_fields = ['name', 'payment_status','phone']


# class SubscriptionViewset(viewsets.ModelViewSet):
#     queryset = models.PaymentRecords.objects.all()
#     serializer_class = serializers.PaymentSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['member']
