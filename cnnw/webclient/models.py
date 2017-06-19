from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=30)

class Person(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70,blank=False)
    password = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    companies = models.ManyToManyField(Company)
    persons = models.ManyToManyField(Person)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)