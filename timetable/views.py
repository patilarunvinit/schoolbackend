from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import timetableserializer
from .models import tt


# Create your views here.

@csrf_exempt
def timetable(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = timetableserializer(data=data1)
        print(outdata)
        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.error, safe=False)

    elif request.method == "GET":
        stand = request.GET['stand']
        print(stand)
        output = tt.objects.all().filter(stand=stand)
        outdata = timetableserializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)
