from django.http import HttpResponse
from django.shortcuts import render
from user.Sources.randomUser import RandomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    message = "Hello"
    return HttpResponse(message)
check_status = lambda data_status : status.HTTP_500_INTERNAL_SERVER_ERROR if data_status != 200 else status.HTTP_200_OK

@api_view(['GET'])
def findRandomUser(request):
    if request.method == 'GET':
        random = RandomUser()
        data = request.GET
        all_user_random = random.getAllUserRandom(seed=data['seed'], country=data['country'], count=int(data['count']))
        status_returns = check_status(all_user_random['status'])
        result = []
        if status_returns == status.HTTP_200_OK:
            result = all_user_random['content']
        return Response(data=result, content_type='JSON', status=status_returns)
        