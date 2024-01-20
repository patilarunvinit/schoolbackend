from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import TeacherFilerSerializer,CompPostSerializer
from .models import CompModel
from django.utils import timezone



@csrf_exempt
def complaintForm(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = CompPostSerializer(data=data1)
        print(outdata)

        if outdata.is_valid():
            outdata.save()
            return JsonResponse({"massage":"data pass"}, safe=False)
        else:
            return JsonResponse({"massage": "data not pass"}, safe=False)





@csrf_exempt
def teacherComp(request):
    if request.method == "GET":
        teacher_name = request.GET['teacher_name']
        sdata = CompModel.objects.all().filter(teacher_name=teacher_name)
        s1data = TeacherFilerSerializer(sdata, many=True)
        return JsonResponse(s1data.data, safe=False)


@csrf_exempt
def ComDeleteById(request):
    if request.method == "GET":
        id = request.GET['id']
        sdata = CompModel.objects.all().filter(id=id)
        sdata.delete()
        return JsonResponse({"massage":"work"}, safe=False)





@csrf_exempt
def notificationSdata(request):
    if request.method == "GET":
        name = request.GET['name']
        class_div = request.GET['class_div']

        output = CompModel.objects.all().filter(name=name,class_div=class_div).order_by("date")
        notifiCount=len(output)
        outdata = TeacherFilerSerializer(output, many=True)
        return JsonResponse({"data":outdata.data,"noticount":notifiCount}, safe=False)
