from .models import sinfo
from rest_framework import serializers




class sinfoserializer(serializers.Serializer):
    username = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=60)
    mother = serializers.CharField(max_length=15)
    class_div = serializers.CharField(max_length=10)
    roll_no = serializers.CharField(max_length=5)
    reg_no = serializers.CharField(max_length=30)
    mobile_no = serializers.CharField(max_length=13)
    b_day = serializers.DateField()
    address = serializers.CharField(max_length=200)
    image = serializers.ImageField()


    class Meta:
        model = sinfo
        fields = ("username","name", "mother", "class_div", "roll_no", "reg_no", "mobile_no","b_day","address","image")

    def create(self, validated_data):
        return sinfo.objects.create(**validated_data)


class teacherattendserializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    roll_no = serializers.CharField(max_length=5)
    class_div = serializers.CharField(max_length=13)
    option = serializers.BooleanField(source='option1')
    teacher_name=serializers.CharField(source='teacher_name1')
    date=serializers.DateField(source='date1')

    class Meta:
        model = sinfo
        fields = ("name", "roll_no", "class_div","option","teacher_name","teacher_name","date")

    def create(self, validated_data):
        return sinfo.objects.create(**validated_data)





class StudFilterserializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


    class Meta:
        model = sinfo
        fields = ("name")

    def create(self, validated_data):
        return sinfo.objects.create(**validated_data)