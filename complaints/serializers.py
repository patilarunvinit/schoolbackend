from .models import CompModel
from rest_framework import serializers
from django.utils import timezone





class CompPostserializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=50)
    class_div = serializers.CharField(max_length=10)
    date = serializers.DateField()
    complaint = serializers.CharField(max_length=500)



    class Meta:
        model = CompModel
        fields = ("teacher_name","name", "class_div", "date", "complaint")

    def create(self, validated_data):
        return CompModel.objects.create(**validated_data)



class TeacherFilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompModel
        fields = '__all__'