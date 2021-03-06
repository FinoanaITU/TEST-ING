from django.http import HttpResponse
from django.shortcuts import render
from user.Sources.randomUser import RandomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.Sources.userManager import UserManager
from django.views.decorators.csrf import csrf_exempt

def index(request):
    message = "Hello"
    return HttpResponse(message)

check_status = lambda data_status : status.HTTP_500_INTERNAL_SERVER_ERROR if data_status != 200 else status.HTTP_200_OK

@csrf_exempt
@api_view(['GET'])
def findRandomUser(request):
    if request.method == 'GET':
        random = RandomUser()
        data = request.GET
        all_user_random = random.getAllUserRandom(seed=data['seed'], country=data['country'], count=int(data['count']))
        status_returns = check_status(all_user_random['status'])
        user_add = 0
        data_base = []
        if status_returns == status.HTTP_200_OK:
            result = all_user_random['content']
            ##save user random
            user_manager = UserManager()
            user_add = user_manager.addUser(result['results'])
            data_base = user_manager.getAllUser()
        resutl = {'user_add': user_add, 'result': data_base }
        return Response(data=resutl, content_type='JSON', status=status_returns)
        