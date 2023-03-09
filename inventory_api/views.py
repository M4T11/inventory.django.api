from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from inventory_api.models import *
from inventory_api.serializers import *

# Create your views here.

# class ListPostLocations(ListCreateAPIView):
#     serializer_class = LocationSerializer
#     queryset = LocationModel.objects.all()
#
# class LocationGetUpdateDeleteID(RetrieveUpdateDestroyAPIView):
#     serializer_class = LocationSerializer
#     queryset = LocationModel.objects.all()

class LocationList(APIView):
    def get(self, request):
        locations = LocationModel.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            # if (LocationModel.objects.get(name=request.data['name'])):
            #     return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):

    def get(self, request, pk):
        location = get_object_or_404(LocationModel, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
        location = get_object_or_404(LocationModel, pk=pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        location = get_object_or_404(LocationModel, pk=pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProducerList(APIView):
    def get(self, request):
        producers = ProducerModel.objects.all()
        serializer = ProducerSerializer(producers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            if (ProducerModel.objects.get(name=request.data['name'])):
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerDetail(APIView):

    def get(self, request, pk):
        producer = get_object_or_404(ProducerModel, pk=pk)
        serializer = ProducerSerializer(producer)
        return Response(serializer.data)

    def put(self, request, pk):
        producer = get_object_or_404(ProducerModel, pk=pk)
        serializer = ProducerSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producer = get_object_or_404(ProducerModel, pk=pk)
        producer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            if (CategoryModel.objects.get(name=request.data['name'])):
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):

    def get(self, request, pk):
        category = get_object_or_404(CategoryModel, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(CategoryModel, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(CategoryModel, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EanDeviceList(APIView):
    def get(self, request):
        ean_devices = EanDeviceModel.objects.all()
        serializer = EanDeviceSerializer(ean_devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EanDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EanDeviceDetail(APIView):

    def get(self, request, pk):
        ean_device = get_object_or_404(EanDeviceModel, pk=pk)
        serializer = EanDeviceSerializer(ean_device)
        return Response(serializer.data)

    def put(self, request, pk):
        ean_device = get_object_or_404(EanDeviceModel, pk=pk)
        serializer = EanDeviceSerializer(ean_device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ean_device = get_object_or_404(EanDeviceModel, pk=pk)
        ean_device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







