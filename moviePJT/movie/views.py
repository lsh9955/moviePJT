from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

class LatestProductsList(APIView):
    def get(self, request, format = None):
        movies = Movie.objects.all()[0:4]
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)


