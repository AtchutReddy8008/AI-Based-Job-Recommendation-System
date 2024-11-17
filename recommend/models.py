from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
