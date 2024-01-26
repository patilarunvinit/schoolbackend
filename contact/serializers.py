from .models import contactmodel
from rest_framework import serializers


class contactserializers(serializers.ModelSerializer):
    class Meta:
        model = contactmodel
        fields = ("name", "email", "massage")

    def create(self, validated_data):
        return contactmodel.objects.create(**validated_data)