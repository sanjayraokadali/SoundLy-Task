from django.db import models


# Create your models here.
class QueryModel(models.Model):

    name = models.CharField(max_length=264)
    email = models.EmailField()
    number = models.IntegerField()
    query = models.TextField(max_length=260)

    def __str__(self):

        return self.name

class GenerateItem(models.Model):

    item_name = models.CharField(max_length=30)

    item_price = models.CharField(max_length=10)

    item_pic = models.ImageField(upload_to='item_pics',blank=False)

    item_url = models.URLField(blank=False)

    def __str__(self):

        return self.item_name

class UserRegistrationModel(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):

        return self.first_name
