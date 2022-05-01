from rest_framework.serializers import ModelSerializer
from .models import Info, Image

class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class InfoSerializer(ModelSerializer):
    images = ImagesSerializer(many = True)

    class Meta:
        model = Info
        fields = '__all__'