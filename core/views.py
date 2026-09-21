from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ContactSerializer, JobSerializer, SiteDetailSerializer
# Create your views here.
from .emails import *
from rest_framework.decorators import api_view, permission_classes
from .models import  SiteDetail
@api_view(['POST'])
def contact_view(request, *args, **kwargs):
    serializer = ContactSerializer(data=request.data, context={'request': request})
    data = {}
    if serializer.is_valid():
        serializer = serializer.save()
        data['message'] = "Thanks for contacting c2constructsecurityltd, your we will respond shortly"
        data['email'] = serializer.email
        send_otp_via_email(serializer.email)
        send_contact_via_emailtoadmin(serializer)
        return Response(data, status=201)
    data = serializer.errors
    return Response(data, status=400)

@api_view(['POST'])
def services_view(request, *args, **kwargs):
    serializer = JobSerializer(data=request.data, context={'request': request})
    data = {}
    if serializer.is_valid():
        serializer = serializer.save()
        data['message'] = "Thanks for contacting c2constructsecurityltd, your we will respond shortly"
        data['email'] = serializer.email
        send_otp_via_email(serializer.email)
        send_job_via_emailtoadmin(serializer)
        return Response(data, status=201)
    data = serializer.errors
    return Response(data, status=400)


@api_view(['GET'])
def siteDataView(request, *args, **kwargs):
    qs = SiteDetail.objects.all()
    if qs:
        qs.first()
        serializer = SiteDetailSerializer(qs, many=True)
        return Response(serializer.data, status=200)
    return Response({}, status=400)

