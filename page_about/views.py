from re import S
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InfoSerializer
from .models import Info
from api import serializers


@api_view(['GET'])  
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/info/',
            'method' : 'GET',
            'title_ru' : None,
            'title_text_ru' : None,
            'title_en' : None,
            'title_text_en' : None,
            'title_kg' : None,
            'title_text_kg' : None,
            'description': 'Returns an array of info/posts'
        },
        {
            'Endpoint': '/info/id/',
            'method' : 'GET',
            'title_ru' : None,
            'title_text_ru' : None,
            'title_en' : None,
            'title_text_en' : None,
            'title_kg' : None,
            'title_text_kg' : None,
            'decsription': 'Returns a single info/post'
        },
        {
            'Endpoint': '/notes/create/',
            'method' : 'POST',
            'title_ru' : None,
            'title_text_ru' : None,
            'title_en' : None,
            'title_text_en' : None,
            'title_kg' : None,
            'title_text_kg' : None,
            'description': 'Creates new info/post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method' : 'PUT',
            'title_ru': {'title_ru': ""},
            'title_text_ru': {'title_text_ru': ""},
            'title_en': {'title_en': ""},
            'title_text_en': {'title_text_en': ""},
            'title_kg': {'title_kg': ""},
            'title_text_kg': {'title_text_kg': ""},
            'description': 'Updates an existing info/post with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method' : 'DELETE',
            'title_ru' : None,
            'title_text_ru' : None,
            'title_en' : None,
            'title_text_en' : None,
            'title_kg' : None,
            'title_text_kg' : None,
            'description': 'Deletes an existing info/post'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getInfo(request):
    info=Info.objects.all()
    serializer = InfoSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleInfo(request, pk):
    singleinfo = Info.objects.get(id=pk)
    serializer = InfoSerializer(singleinfo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createInfo(request):
    data=request.data

    info = Info.objects.create(
        title_ru = data['title_ru'],
        title_text_ru = data['title_text_ru'],
        title_en = data['title_en'],
        title_text_en = data['title_text_en'],
        title_kg = data['title_kg'],
        title_text_kg = data['title_text_kg'],
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