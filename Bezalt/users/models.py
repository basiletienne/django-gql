from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#pip freeze > requirements.txt
# front end : take token from link end send it to server
# need to setup email backend

class ExtendUser(AbstractUser) :
    email = models.EmailField(blank=False, max_length=128, verbose_name='email')

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

