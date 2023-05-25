from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('date', 'time', 'occupied',)


class RecordOccupiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('occupied',)

