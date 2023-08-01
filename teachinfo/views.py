from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import tinfoserializer
from .models import tinfo



from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.



@csrf_exempt
@permission_classes((AllowAny,))
def loginT(request):
   if request.method == "POST":
       data2 = JSONParser().parse(request)
       username = data2["username"]
       password = data2["password"]
       print(username,password)
       counter=tinfo.objects.filter(username=username)

       if username=="" or password =="":
           return JsonResponse({'error': 'Please provide both username and password'},
                           status=HTTP_400_BAD_REQUEST)
       user = authenticate(username=username, password=password)
       if not user:
           return JsonResponse({'error': 'Invalid Credentials'},
                           status=HTTP_404_NOT_FOUND)
       else:
           if counter:
               login(request, user)
               request.session['email'] = user.email
               token, _ = Token.objects.get_or_create(user=user)
               sdata = tinfo.objects.filter(username=username)
               s1data = tinfoserializer(sdata, many=True)
               return JsonResponse({'token': token.key, "massage": "logged in successfuly", "Sdata": s1data.data})

           else:
               return JsonResponse({'error': 'WRONG LOGIN'},
                                   status=HTTP_404_NOT_FOUND)

