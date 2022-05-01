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
            'desc_ru' : None,
            'title_en' : None,
            'desc_en' : None,
            'title_kg' : None,
            'desc_kg' : None,
            'gallery_id' : None,
            'description': 'Returns an array of info/posts'
        },
        {
            'Endpoint': '/info/id/',
            'method' : 'GET',
            'title_ru' : None,
            'desc_ru' : None,
            'title_en' : None,
            'desc_en' : None,
            'title_kg' : None,
            'desc_kg' : None,
            'gallery_id' : None,
            'decsription': 'Returns a single info/post'
        },
        {
            'Endpoint': '/notes/create/',
            'method' : 'POST',
            'title_ru' : None,
            'desc_ru' : None,
            'title_en' : None,
            'desc_en' : None,
            'title_kg' : None,
            'desc_kg' : None,
            'gallery_id' : None,
            'description': 'Creates new info/post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method' : 'PUT',
            'title_ru': {'title_ru': ""},
            'desc_ru': {'desc_ru': ""},
            'title_en': {'title_en': ""},
            'desc_en': {'desc_en': ""},
            'title_kg': {'title_kg': ""},
            'desc_kg': {'desc_kg': ""},
            'gallery_id': {'gallery_id': ""},
            'description': 'Updates an existing info/post with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method' : 'DELETE',
            'title_ru' : None,
            'desc_ru' : None,
            'title_en' : None,
            'desc_en' : None,
            'title_kg' : None,
            'desc_kg' : None,
            'gallery_id' : None,
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
        desc_ru = data['desc_ru'],
        title_en = data['title_en'],
        desc_en = data['desc_en'],
        title_kg = data['title_kg'],
        desc_kg = data['desc_kg'],
        gallery_id = data['gallery_id'],
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