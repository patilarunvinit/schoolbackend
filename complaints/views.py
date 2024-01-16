from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import CompPostserializer,TeacherFilerSerializer
from .models import CompModel



@csrf_exempt
def complaintForm(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = CompPostserializer(data=data1)
        print(outdata)
        if outdata.is_valid():
            outdata.save()
            return JsonResponse({"massage":"data pass"}, safe=False)
        else:
            return JsonResponse({"massage": "data not pass"}, safe=False)



def teacherComp(request):
    if request.method == "GET":
        teacher_name = request.GET['teacher_name']
        sdata = CompModel.objects.all().filter(teacher_name=teacher_name)
        s1data = TeacherFilerSerializer(sdata, many=True)
        return JsonResponse(s1data.data, safe=False)


def ComDeleteById(request):
    if request.method == "GET":
        id = request.GET['id']
        sdata = CompModel.objects.all().filter(id=id)
        sdata.delete()
        return JsonResponse({"massage":"work"}, safe=False)

