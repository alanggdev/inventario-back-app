from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import InventorySerializer
from .models import InventoryModel
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def custom_response(msg, response, status):
    data ={
        "messages": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

class InventoryCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class InventoryListView(APIView):
    def get(self, request):
        queryset = InventoryModel.objects.all()
        serializer = InventorySerializer(queryset, many=True ,context={'request':request})
        return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    
class InventoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return InventoryModel.objects.get(pk = pk)  
        except InventoryModel.DoesNotExist:   
            return 0
        
    def get(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive != 0:
            serializer = InventorySerializer(objetive)
            return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
        
    def patch(self, request, pk, format = None):
        objetive = self.get_object(pk)
        serializer = InventorySerializer(objetive, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(custom_response("Error", serializer.errors, status=status.HTTP_404_NOT_FOUND))
    
    def delete(self, request, pk, format = None):
        objetive = self.get_object(pk)
        if objetive != 0:
            objetive.delete()
            return Response(custom_response("Success", "Deleted", status=status.HTTP_200_OK))
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
    
class InventoryPerOwner(APIView):
    def get(self, request, id_owner, format=None):
        queryset = InventoryModel.objects.filter(owner=id_owner)
        if len(queryset) != 0:
            serializer = InventorySerializer(queryset, many=True, context={'request': request})
            return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
    
class InventoryPerAdmin(APIView):
    def get(self, request, id_admin, format=None):
        queryset = InventoryModel.objects.filter(admins=id_admin)
        if len(queryset) != 0:
            serializer = InventorySerializer(queryset, many=True, context={'request': request})
            return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
    
class InventoryPerSeller(APIView):
    def get(self, request, id_seller, format=None):
        queryset = InventoryModel.objects.filter(sellers=id_seller)
        if len(queryset) != 0:
            serializer = InventorySerializer(queryset, many=True, context={'request': request})
            return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
    
class GetUser(APIView):
    def get(self, request, username, format=None):
        try:
            user = User.objects.get(username__iexact=username).id
            return Response(custom_response("Success", user, status=status.HTTP_200_OK))
        except ObjectDoesNotExist:
            return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
        
class GetUsername(APIView):
    def get(self, request, id, format=None):
        try:
            user = User.objects.get(id=id).username
            return Response(custom_response("Success", user, status=status.HTTP_200_OK))
        except ObjectDoesNotExist:
            return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))