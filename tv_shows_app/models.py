from django.db import models
from django.db.models.fields import DateTimeField,DateField
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if postData['title'] == "" or postData['network'] == "" or postData['release_date'] == "":
            errors['all_fields'] = "All fields are required"
        if postData['title'] != "" and len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if postData['network'] != "" and len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"
        if postData['release_date'] != "":
            x = postData['release_date']
            # release_date = int(x[0:4]+x[5:7]+x[8:10])
            # now = int(datetime.today().strftime('%Y%m%d'))
            now = datetime.now()
            release_date = datetime.strptime(x,'%Y-%m-%d') 
            if release_date > now: 
                errors['release_date'] = "Release date should be in the past"  #release_date = ",str(release_date),str(type(release_date)),"now = ",str(now),str(type(now)),x,str(type(x))
        if postData['hidden'] == "new_show":
            # for show in Show.objects.all():
            #     if show.title == postData['title']:
            if Show.objects.filter(title=postData['title']):
                errors['duplicate_title'] = "Show with that title already exists"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
