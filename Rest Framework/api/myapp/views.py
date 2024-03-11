from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StudentSerializers

# Create your views here.

@api_view(["GET"])
def studentAll(request):
    if request.method=="GET":
        studentall=Student.objects.all()
        serializer=StudentSerializers(studentall,many=True)
        return Response(serializer.data)

@api_view(["POST"])    
def studentAdd(request):
    if request.method=="POST":
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def student(request,pk):
    student=Student.objects.get(id=pk)
    if request.method == "GET":
        serializer=StudentSerializers(student)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)