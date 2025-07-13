from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Farm,Crop,Animal
from .serializers import FarmSerializer,CropSerializer,AnimalSerializer
from .permissions import IsOwnerOrReadOnly
class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Crop.objects.filter(farm__owner=self.request.user)

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Animal.objects.filter(farm__owner=self.request.user)