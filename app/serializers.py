from rest_framework import serializers
from .models import Users, Pets

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'