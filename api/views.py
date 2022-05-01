from re import S
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import InfoSerializer
from .models import Info
from api import serializers
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class UserAuth(APIView):
    def post(self, request):

        user = authenticate(
            username = request.data.get("username"),
            password = request.data.get("password"))
        if user is not None:
            try:
                token = Token.objects.get(user=user)
                print(token.key)
                print(user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
                print(token.key)
                print(user)
            return Response(token.key)
        else:
            return Response([], status=HTTP_401_UNAUTHORIZED)


class UserRegister(APIView):
    def post(self, request):

        user = User.objects.create_user(
            username=request.data.get("username"),
            email=request.data.get("email"),
            password=request.data.get("password"))
        user.save()

        if user is not None:
            token = Token.objects.create(user=user)
            print(token.key)
            print(user)
            return Response(token.key)
        else:
            return Response([], status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])  
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/info/',
            'method' : 'GET',
            'body' : None,
            """'price': None,"""
            'description': 'Returns an array of info/posts'
        },
        {
            'Endpoint': '/info/id/',
            'method' : 'GET',
            'body' : None,
            """'price': None,"""
            'decsription': 'Returns a single info/post'
        },
        {
            'Endpoint': '/notes/create/',
            'method' : 'POST',
            'body': None,
            """'price': None,"""
            'description': 'Creates new info/post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method' : 'PUT',
            'body': {'body': ""},
            """'price': {'price': ""},""" 
            'description': 'Updates an existing info/post with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method' : 'DELETE',
            'body': None, 
            """'price': None,"""
            'description': 'Deletes an existing info/post'
        }
    ]
    return Response(routes)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getInfo(request):
    info=Info.objects.all()
    serializer = InfoSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getSingleInfo(request, pk):
    singleinfo = Info.objects.get(id=pk)
    serializer = InfoSerializer(singleinfo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createInfo(request):
    data=request.data
    info = Info.objects.create(
        body = data['body'],
    )
    serializer = InfoSerializer(info, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateInfo(request, pk):
    data=request.data

    info = Info.objects.get(id=pk)

    serializer = InfoSerializer(info, data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteInfo(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return Response('Post deleted successfully')