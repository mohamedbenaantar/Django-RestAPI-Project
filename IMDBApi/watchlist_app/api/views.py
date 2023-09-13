from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlateform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .permissions import AdminOrReadOnly

class StreamPlateformAV(APIView):
     permission_classes = [AdminOrReadOnly]
    
     def get(self, request):
         plateform = StreamPlateform.objects.all()
         serializer = StreamPlateformSerializer(plateform, many=True)
         return Response(serializer.data)
     
     def post(self, request):
         serializer = StreamPlateformSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data) 