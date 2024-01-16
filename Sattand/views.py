from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import attandmodserializer, TfilterSserializer , TfilterDserializer
from .models import attandmodN




# Create your views here.
@csrf_exempt
def attandForS(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        lenn=len(data1)
        print(lenn)
        counter=1
        for i in range(lenn):
            print(data1[i])
            outdata = attandmodserializer(data=data1[i])
            if outdata.is_valid():
                outdata.save()

            else:
                counter=0

        if counter == 1:
            return JsonResponse({"massage":"data pass"}, safe=False)
        else:
            return JsonResponse({"massage": "data not pass"}, safe=False)


    elif request.method == "GET":
        sdata = attandmodN.objects.all()
        s1data = attandmodserializer(sdata, many=True)
        return JsonResponse(s1data.data, safe=False)



@csrf_exempt
def Tfiltertostand(request):
    if request.method == "GET":
        name = request.GET['name']
        output = attandmodN.objects.all().filter(teacher_name=name).order_by("class_div").values("class_div").distinct()
        outdata = TfilterSserializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)


@csrf_exempt
def Tfiltertodate(request):
    if request.method == "GET":
        name = request.GET['name']
        class_div = request.GET['class_div']

        output = attandmodN.objects.all().filter(teacher_name=name,class_div=class_div).order_by("date").values("date").distinct()
        outdata = TfilterDserializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)


@csrf_exempt
def Sattendence(request):
    if request.method == "GET":
        name = request.GET['name']
        class_div = request.GET['class_div']

        output = attandmodN.objects.all().filter(name=name,class_div=class_div).order_by("date")
        outdata = attandmodserializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)



@csrf_exempt
def checkback(request):
    if request.method == "GET":
        name = request.GET['name']
        class_div = request.GET['class_div']
        date = request.GET['date']


        output = attandmodN.objects.all().filter(teacher_name=name,class_div=class_div,date=date)
        outdata = attandmodserializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)


@csrf_exempt
def percentageCAl(request):
    if request.method == "GET":
        name = request.GET['name']
        class_div = request.GET['class_div']


        output = attandmodN.objects.all().filter(name=name,class_div=class_div)
        all=len(output)
        attand=0
        for i in range(all):
            if output[i].option == True:
                attand+=1

            else:
                pass

        div=attand/all
        percentage=div*100
        print(percentage)
        return JsonResponse({"percentage":percentage}, safe=False)