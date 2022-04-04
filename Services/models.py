from distutils import text_file
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    desc = models.CharField(max_length=2500, blank=True)
    content = models.TextField()
    image = models.ImageField(
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
        blank=True
    )
    
    def __str__(self):
        return self.title


class MessageService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return str(self.service)