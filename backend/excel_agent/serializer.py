from rest_framework import serializers

# Create a serializer
class ExcelTaskSerializer(serializers.Serializer):
    instruction = serializers.CharField()
    file = serializers.FileField()