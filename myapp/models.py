
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    video = models.FileField(upload_to='gallery_videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title
    
#users model
class PrivitasationUsers(models.Model):
    email=models.EmailField()
    password= models.TextField()
    name=models.CharField(max_length=30,null=True)
    kra=models.TextField(null=True)
    phone=models.TextField(null=True)
    company=models.TextField(null=True)


    def __str__(self):
        return self.email
    
class AvailableOpening(models.Model):
    no = models.IntegerField()
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title



