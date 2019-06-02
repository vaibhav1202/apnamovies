from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_img(upload): 
      ext = upload.name[-4:]
      if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')    
      if upload.size > 1024*1024*2:
        raise ValidationError(u'File too big!')    

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_cast  = models.TextField()
    description  = models.TextField()
    img=models.ImageField(upload_to = "images\\", validators=[validate_img], null=True, blank=True)    
    ulink = models.URLField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=50, null=True)    
    genre = models.CharField(max_length=40 ,choices=(("Comedy","Comedy"), ("Horor","Horor"), ("SciFi","SciFi"), ("Action","Action"), ("Drama","Drama"), ("Romantic","Romantic"), ("Other","Other")))    
    def __str__(self):
        return "%s (%s)" % (self.name, self.genre)
