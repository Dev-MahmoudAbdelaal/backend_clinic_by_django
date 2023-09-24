from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Post_Doctor_Serializer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from .models import Doctor
from rest_framework import generics
from rest_framework import mixins
    
class PostList_Doctor(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    queryset = Doctor.postobjects.all()
    serializer_class = Post_Doctor_Serializer
    pass


class PostDetail_Doctor(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    permission_classes=[AllowAny]
    queryset = Doctor.objects.all()
    serializer_class = Post_Doctor_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)