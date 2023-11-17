from rest_framework import serializers
from watchlist_app.models import StreamPlateform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)  ### 
        
class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    plateform = serializers.CharField(source='plateform.name')
    class Meta:
        model = WatchList
        fields = "__all__"
    
    
class StreamPlateformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlateform
        fields = "__all__"
        
    
    