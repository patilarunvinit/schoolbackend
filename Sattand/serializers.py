from .models import attandmodN
from rest_framework import serializers




class attandmodserializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=60)
    class_div = serializers.CharField(max_length=10)
    roll_no = serializers.CharField(max_length=5)
    option = serializers.BooleanField()
    date = serializers.DateField()



    class Meta:
        model = attandmodN
        fields = ("teacher_name","name", "class_div", "roll_no","option", "date")

    def create(self, validated_data):
        return attandmodN.objects.create(**validated_data)


class TfilterSserializer(serializers.Serializer):
    class_div = serializers.CharField(max_length=10)
    class Meta:
        model = attandmodN
        fields = ("class_div")

    def create(self, validated_data):
        return attandmodN.objects.create(**validated_data)


class TfilterDserializer(serializers.Serializer):
    date = serializers.DateField()
    class Meta:
        model = attandmodN
        fields = ("date")

    def create(self, validated_data):
        return attandmodN.objects.create(**validated_data)