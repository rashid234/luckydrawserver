from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserRegister
from .serializers import CustomAuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class register(APIView):

    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response'] = 'registered'
            data['username'] = account.username
            token,create = Token.objects.get_or_create(user = account)
            data['token'] = token.key
        else:
            data=serializer.errors
        return Response(data)

class leads(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        content = {
            'user': str(request.user),
            'userid': str(request.user.id),
            'email': str(request.user.email)
        }
        return Response(content)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})