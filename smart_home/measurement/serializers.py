from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
