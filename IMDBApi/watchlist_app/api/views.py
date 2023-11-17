from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlateform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttling import ReviewCreateThrottle, ReviewListThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from watchlist_app.api.pagination import WatchListPagination

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        ## pk of the watchlist reviewed
        watchlist = WatchList.objects.get(pk=pk)

        author = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, author=author)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, author=author)
        
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__username', 'active'] 
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    

class StreamPlateformVS(viewsets.ModelViewSet):
    queryset = StreamPlateform.objects.all()
    serializer_class = StreamPlateformSerializer
    permission_classes = [AdminOrReadOnly]
    
class StreamPlateformDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            plateform = StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'Error': 'Plateform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlateformSerializer(plateform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        plateform = StreamPlateform.objects.get(pk=pk)
        serializer = StreamPlateformSerializer(plateform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        plateform = StreamPlateform.objects.get(pk=pk)
        plateform.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
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
    permission_classes = [AdminOrReadOnly]
    
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