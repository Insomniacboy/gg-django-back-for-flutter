from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField
from .models import Info, SubInfo

class SubInfoSerializer(ModelSerializer):
    class Meta:
        model = SubInfo
        fields = '__all__'

class InfoSerializer(ModelSerializer):
    subcategories = SubInfoSerializer(many = True)
    
    class Meta:
        model = Info
        fields = '__all__'