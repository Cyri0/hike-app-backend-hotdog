from django.db import models

# Create your models here.
class Hike(models.Model):

    kep = models.CharField(max_length=150)
    cim = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cim

class Review(models.Model):

    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField()
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname