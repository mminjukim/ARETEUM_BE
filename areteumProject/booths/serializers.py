from rest_framework import serializers 
from .models import *


class BoothSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Booth 
        fields = '__all__'

class Day1BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['id', 'name', 'place', 'time_day1']

class Day2BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['id', 'name', 'place', 'time_day2']

class SearchBoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['id', 'name', 'place', 'time_day1', 'time_day2']


class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroup
        fields = '__all__'
        

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'