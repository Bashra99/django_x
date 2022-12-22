from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser
# Create your models here.

class AOT(models.Model):
    name=models.CharField(max_length=64,help_text='Character Name',default='AOT')
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField(default='description')
    img_url = models.TextField(default="NO Image")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('aot_detail', args=[str(self.id)])

