from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
#to make sure that user input images of jpg, jpeg and png and dont allow other extensions or videos 
from django.core.validators import FileExtensionValidator

class ProfileModel(models.Model):
    # make relation between user model and profile model as each user has one profile
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='image/default.jpg',upload_to='profile',validators=[FileExtensionValidator(['png','jpg','jpeg'])])

#name the objects in database by user name
    def __str__(self):
        return self.user.username


