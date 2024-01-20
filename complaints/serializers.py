from .models import CompModel
from rest_framework import serializers
from django.utils import timezone






class TeacherFilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompModel
        fields = '__all__'




class CompPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompModel
        fields = ("teacher_name", "name", "class_div", "date", "complaint", "mobile_no", "complaint_date1")

    def create(self, validated_data):
        return CompModel.objects.create(**validated_data)




"""class CompPostserializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=50)
    class_div = serializers.CharField(max_length=10)
    date = serializers.DateField()
    complaint = serializers.CharField(max_length=500)
    mobile_no=serializers.CharField(max_length=10)
    complaint_date1 = serializers.DateTimeField()




    class Meta:
        model = CompModel
        fields = ("teacher_name","name", "class_div", "date", "complaint","mobile_no","complaint_date1")

    def create(self, validated_data):
        return CompModel.objects.create(**validated_data)"""