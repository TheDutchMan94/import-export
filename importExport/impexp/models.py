from os import name
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=SET_NULL, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Blogcategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Blogcategory, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField()
    uploaded_by = models.CharField(default="Admin", max_length=150)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Aboutus(models.Model):
    whoarewe = models.TextField()
    ourvision = models.TextField()

    def __str__(self):
        return self.whoarewe


class Contactus(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField()
    website = models.URLField()

    def __str__(self):
        return self.name