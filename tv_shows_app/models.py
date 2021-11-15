from django.db import models
from django.db.models.fields import DateTimeField,DateField
from datetime import *

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if postData['title'] == "" or postData['network'] == "" or postData['release_date'] == "" or postData['description'] == "":
            errors['all_fields'] = "All fields are required"
        if postData['title'] != "" and len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if postData['network'] != "" and len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if postData['description'] != "" and len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"
        if postData['release_date'] != "":
            x = postData['release_date']
            release_date = int(x[0:4]+x[5:7]+x[8:10])
            today = int(datetime.today().strftime('%Y%m%d'))
            if release_date > today:
                errors['release_date'] = "Release date should be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
