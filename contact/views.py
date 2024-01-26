from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import contactserializers


# Create your views here.

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data1 = JSONParser().parse(request)
        outdata = contactserializers(data=data1)
        print(outdata)

        if outdata.is_valid():
            outdata.save()
            return JsonResponse({"massage": "data pass"}, safe=False)
        else:
            return JsonResponse({"massage": "data not pass"}, safe=False)