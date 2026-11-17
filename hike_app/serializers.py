from rest_framework import serializers

from .models import Hike, Review

class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 1