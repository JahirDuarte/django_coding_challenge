from rest_framework import serializers
from .models import EmailsSentRegister

class EmailsSentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailsSentRegister
        fields = '__all__'
