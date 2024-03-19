from rest_framework import serializers
from demoapp.models import UserInfo
from demoapp.models import Financial


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = '__all__'
