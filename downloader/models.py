from django.db import models
from PIL import Image

class WebSite(models.Model):

    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    image = models.FileField(upload_to='web_logo', max_length=100)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'WebSite'
        verbose_name_plural = 'WebSites'