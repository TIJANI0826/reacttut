from django.shortcuts import render
from .models import Grocery
from .serializers import GroceryCategorySerializer,GrocerySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from rest_framework.utils import serializer_helpers


from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    GenericAPIView
)
from .pagination import GroceryPagination
# Create your views here.

class GroceryView(viewsets.ModelViewSet):
    serializer_class = GrocerySerializer
    queryset = Grocery.objects.all()

@api_view(["GET","POST"])
def grocery_list(request):
    if request.method == "GET":
        data = Grocery.objects.all()

        serializer = GrocerySerializer(data,context={'request': request},many=True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT","DELETE"])
def grocery_detail(request,pk):
    try:
        grocery = Grocery.object.get(pk=pk)
    except Grocery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = GrocerySerializer(grocery,data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        grocery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

