from rest_framework import serializers
from .models import Person, CarAccident

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CarAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAccident
        fields = '__all__'
