from rest_framework import generics
from .models import Movie, Attend
from .serializers import MovieSerializer, AttendSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AttendListView(generics.ListCreateAPIView):
    queryset = Attend.objects.all()
    serializer_class = AttendSerializer


class AttendSummaryView(generics.ListAPIView):
    queryset = Attend.objects.all()
    serializer_class = AttendSerializer
