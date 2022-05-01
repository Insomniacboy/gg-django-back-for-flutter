from re import S
from unicodedata import category
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import InfoSerializer
from .models import Info, Image
from api import serializers



@api_view(['GET'])  
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/info/',
            'method' : 'GET',
            'title' : None,
            'desc' : None,
            'price' : None,
            'phone' : None,
            'category_id' : None,
            'region_id' : None,
            'published' : None,
            'description': 'Returns an array of info/posts'
        },
        {
            'Endpoint': '/info/id/',
            'method' : 'GET',
            'title' : None,
            'desc' : None,
            'price' : None,
            'phone' : None,
            'category_id' : None,
            'region_id' : None,
            'published' : None,
            'decsription': 'Returns a single info/post'
        },
        {
            'Endpoint': '/notes/create/',
            'method' : 'POST',
            'title' : None,
            'desc' : None,
            'price' : None,
            'phone' : None,
            'category_id' : None,
            'region_id' : None,
            'published' : None,
            'description': 'Creates new info/post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method' : 'PUT',
            'title': {'title': ""},
            'desc': {'desc': ""},
            'price': {'price': ""},
            'phone': {'phone': ""},
            'category_id': {'category_id': ""},
            'region_id': {'region_id': ""},
            'published': {'published': ""},
            'description': 'Updates an existing info/post with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method' : 'DELETE',
            'title' : None,
            'desc' : None,
            'price' : None,
            'phone' : None,
            'category_id' : None,
            'region_id' : None,
            'published' : None,
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
        title = data['title'],
        desc = data['desc'],
        price = data['price'],
        phone = data['phone'],
        category_id = data['category_id'],
        region_id = data['region_id'],
        published = data['published'],
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