from django.db import models


class Chefs(models.Model):
    ChEFS_CHOICES = (
        ("Restaurant Ouner","Restaurant Ouner"),
        ("Head Chef","Head Chef"),
        ("Chef","Chef"),
        
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=ChEFS_CHOICES, default="Chef")
    image = models.ImageField(upload_to='chefs/images/', max_length=250)
    bio = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
