from django.shortcuts import render
from rest_framework import generics
from .models import Sample
from .serializers import ReactSerializer
from rest_framework.response import Response

# Create your views here.
class ReactView(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = ReactSerializer

