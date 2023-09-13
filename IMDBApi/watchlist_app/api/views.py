from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlateform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class WatchListAV(APIView):
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    
    
    def get(self, request):
        movies = WatchList.objects.all()
        #mutiple objects you have you need to add many=True
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # because of the return in create serializer function
        else:
            # content is not valid
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    #permission_classes = [AdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  #jump to or serializer function depends on the method 
            return Response(serializer.data)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_202_ACCEPTED)