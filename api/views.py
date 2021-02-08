from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import meme
from django.views.decorators.csrf import csrf_exempt
from .serializers import MemeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
import requests
# Create your views here.

class MemeAPIView(APIView):

    def get(self,request):
        memes=meme.objects.all().order_by('-id')[:5]
        serializer=MemeSerializer(memes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MemeSerializer(data=request.data)

        if serializer.is_valid():

            nameNew=request.data['name']
            captionNew=request.data['caption']
            urlNew=request.data['url']
            duplicateResult=meme.objects.filter(name=nameNew,caption=captionNew,url=urlNew)

            if duplicateResult.exists():
                return Response("Duplicate Value entered",status=status.HTTP_409_CONFLICT)

            serializer.save()
            return Response({'id':serializer.data['id']},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MemeDetail(APIView):

    def get_object(self,id):
        try:
            return meme.objects.get(id=id)
        except meme.DoesNotExist:
            raise Http404
        
    def get(self,request,id):
        meme=self.get_object(id)
        serializer=MemeSerializer(meme)
        return Response(serializer.data)

    def put(self,request,id):
        meme=self.get_object(id)
        serializer=MemeSerializer(meme,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        meme=self.get_object(id=id)
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,id):
        meme=self.get_object(id=id)
        serializer=MemeSerializer(meme,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        