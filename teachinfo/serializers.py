from .models import tinfo
from rest_framework import serializers




class tinfoserializer(serializers.Serializer):
    username = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=60)
    mother = serializers.CharField(max_length=15)
    employe_id = serializers.CharField(max_length=20)
    mobile_no = serializers.CharField(max_length=13)
    b_day = serializers.DateField()
    address = serializers.CharField(max_length=200)
    image = serializers.ImageField()


    class Meta:
        model = tinfo
        fields = ("username","name", "mother", "employe_id", "mobile_no","b_day","address","image")

    def create(self, validated_data):
        return tinfo.objects.create(**validated_data)