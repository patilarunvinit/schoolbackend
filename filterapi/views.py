from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from studinfo.serializers import sinfoserializer,teacherattendserializer
from studinfo.models import sinfo
# Create your views here.

def test(request):
    if request.method == "GET":
        class_div = request.GET['stand']
        sdata = sinfo.objects.all().filter(class_div=class_div)
        s1data = sinfoserializer(sdata, many=True)
        return JsonResponse(s1data.data, safe=False)


def test1(request):
    if request.method == "GET":
        class_div = request.GET['stand']
        sdata = sinfo.objects.all().filter(class_div=class_div)
        s1data = teacherattendserializer(sdata, many=True)
        return JsonResponse(s1data.data, safe=False)