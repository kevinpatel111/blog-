from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# class author(models.Model):
class author(AbstractUser):
    """
        Custom user model using base class AbstractUser
    """
    
    first_name = None
    last_name = None
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    email =models.EmailField(max_length=80,unique=True)
    phone = models.CharField(max_length=10, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.name

    
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


