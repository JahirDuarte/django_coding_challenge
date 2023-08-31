from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

# Apps modules
from licenses.models import EmailsSentRegister
from licenses.serializers import EmailsSentRegisterSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def HomeView(request):
    emails_sent = EmailsSentRegister.objects.all()
    serializer = EmailsSentRegisterSerializer(emails_sent, many=True)
    return Response(serializer.data)
