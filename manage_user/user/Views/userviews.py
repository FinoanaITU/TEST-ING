import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.Sources.userManager import UserManager
from django.views.decorators.csrf import csrf_exempt

def checkFormat(url):
    format = 'JSON'
    check = re.search('xml', url)
    if check != None:
        format = 'XML'
    return format

@csrf_exempt
@api_view(['GET'])
def getAllUser(request):
    if request.method == 'GET':
        result = ''
        try:
            data = request.GET
            url = request.build_absolute_uri()
            format = checkFormat(url)
            user_manager = UserManager()
            all_user = user_manager.getAllUser() if bool(data) == False else user_manager.getUserComplexFilter(dict(data))
            result = Response(data=all_user, content_type=format, status=status.HTTP_200_OK)
        except Exception as e:
            result =  Response( data = {'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return result

@csrf_exempt    
@api_view(['GET'])
def filterUser(request, uuid):
    if request.method == 'GET':
        result = ''
        try:
            user_manager = UserManager()
            user = user_manager.getUserByUuid(uuid)
            url = request.build_absolute_uri()
            format = checkFormat(url)
            result = Response(data=user, content_type=format, status=status.HTTP_200_OK)
        except Exception as e:
            result =  Response( data = {'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return result
    