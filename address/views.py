from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Post_Address_Serializer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from .models import Address
from rest_framework import generics
from rest_framework import mixins
    
class PostList_Address(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    queryset = Address.postobjects.all()
    serializer_class = Post_Address_Serializer
    pass


class PostDetail_Address(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    permission_classes=[AllowAny]

    queryset = Address.objects.all()
    serializer_class = Post_Address_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)