from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField()
    message = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    gender = models.CharField(max_length=25, blank=False, null=False)
    event = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=False)


    def __str__(self):
        return self.name
