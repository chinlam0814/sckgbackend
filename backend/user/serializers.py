from rest_framework import serializers
from .models import Account, Admin

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admin
        fields = '__all__'