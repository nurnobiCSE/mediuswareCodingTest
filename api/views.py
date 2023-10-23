from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from tasks.models import TaskModel
from .serializer import TaskApiSerializer
# Create your views here.
class TaskApiView(APIView):
    def get(self,request):
        obj = TaskModel.objects.all()
        serializer = TaskApiSerializer(obj, many = True )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TaskApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TaskInfo(APIView):
    def get(self,request,id):
        try:
            obj = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            msg = {"msg": "Not Found !"}    
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskApiSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self,request,id):
        try:
            obj = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            msg = {"msg":"not found error"}    
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskApiSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,id):
        try:
            obj = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            msg = {"msg":"not found error"}    
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskApiSerializer(obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id):
        try:
            obj = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            msg = {"msg":"not found!"}    
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)