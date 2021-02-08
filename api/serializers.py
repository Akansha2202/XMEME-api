from rest_framework import serializers
from .models import meme

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=meme
        fields='__all__'