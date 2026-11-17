from django.urls import path

from . import views

app_name = "hike_app"
urlpatterns = [
    path('hikes/',views.getHikes, name = "getHikes"),
    path('reviews/', views.getReviews)
]
