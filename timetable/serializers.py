from .models import tt
from rest_framework import serializers




class timetableserializer(serializers.Serializer):
    stand = serializers.CharField(max_length=50)
    time = serializers.CharField(max_length=100)
    Monday = serializers.CharField(max_length=50)
    Tuesday = serializers.CharField(max_length=50)
    Wednesday = serializers.CharField(max_length=50)
    Thursday = serializers.CharField(max_length=50)
    Friday = serializers.CharField(max_length=50)
    Saturday = serializers.CharField(max_length=50)

    class Meta:
        model = tt
        fields = ("stand","time","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    def create(self, validated_data):
        return tt.objects.create(**validated_data)