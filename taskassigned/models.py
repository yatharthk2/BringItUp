from django.db import models

# Create your models here.
class featured_ideas(models.Model):
    idea_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()

class features_web(models.Model):
    idea_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()

    




