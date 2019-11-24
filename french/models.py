from django.db import models

# Create your models here.
class French(models.Model):
    name = models.TextField()
    engname = models.TextField()

class Verbir(models.Model):
    irname = models.TextField()
    irengname = models.TextField()

class Verber(models.Model):
    ername= models.TextField()
    erengname= models.TextField()

class Verbre(models.Model):
    rename= models.TextField()
    reengname= models.TextField()

class Phrase(models.Model):
    pname = models.TextField()