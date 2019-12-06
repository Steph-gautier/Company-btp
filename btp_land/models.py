from django.db import models

class Message(models.Model):
    #linked_category = models.ForeignKey('Project',on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    def __str__(self):
        return self.message

class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    details = models.CharField(max_length=150)
    image = models.ImageField(upload_to ='images/')
    description = models.TextField()

    def __str__(self):
        return self.title
