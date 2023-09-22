from rest_framework import serializers
from .models import Movie, Attend

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attend
        fields = '__all__'
