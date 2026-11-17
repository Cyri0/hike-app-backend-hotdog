from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Hike, Review
from .serializers import HikeSerializer, ReviewSerializer

# Create your views here.

@api_view(["GET", "POST"])
def getHikes(request):
    if request.method == "GET":
        allHikes = Hike.objects.all()
        serialized = HikeSerializer(allHikes, many=True)
        return Response(serialized.data)
    else: # Tehát a method POST
        serializer = HikeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def getReviews(request):
    allReviews = Review.objects.all()
    serialized = ReviewSerializer(allReviews, many=True)
    return Response(serialized.data)