from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.Sources.userManager import UserManager

@api_view(['GET'])
def getAllUser(request):
    if request.method == 'GET':
        user_manager = UserManager()
        all_user = user_manager.getAllUser()
        
        return Response(data=all_user, content_type='JSON', status=status.HTTP_200_OK)
    
@api_view(['GET'])
def filterUser(request, uuid):
    if request.method == 'GET':
        user_manager = UserManager()
        user = user_manager.getUserByUuid(uuid)
        
        return Response(data=user, content_type='JSON', status=status.HTTP_200_OK)