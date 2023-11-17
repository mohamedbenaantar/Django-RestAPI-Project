from rest_framework import serializers
from watchlist_app.models import StreamPlateform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        
class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    plateform = serializers.CharField(source='plateform.name')
    class Meta:
        model = WatchList
        fields = "__all__"
    def validate_title(self, value):
        if len(value)<2:
            raise serializers.ValidationError('Name must be at least 2 characters')
        return value
    
    #object level validation
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Name and description cannot be the same')
        return data

class StreamPlateformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlateform
        fields = "__all__"
        
    