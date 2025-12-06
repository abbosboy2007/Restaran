from django.db import models

class Category(models.Model):
    
    STATUS_CHOICES = [
            ('Ertalab', 'Ertalab'),
            ('Abet', 'Abet'),
            ('Tushlik', 'Tushlik'),
            ('Ichimliklar', 'Ichimliklar'),
            ('Shirinliklar', 'Shirinliklar'),
        ]
    title  = models.CharField(max_length=200, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Manls(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name