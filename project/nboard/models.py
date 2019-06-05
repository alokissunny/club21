from django.db import models

# Create your models here.
class Notice(models.Model):
    content = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published')
    severity = models.IntegerField(default = 0)
    def __str__(self):
        return self.content
class rwa(models.Model):
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length = 200)
    pincode = models.IntegerField()
    subscriptionType = models.CharField(max_length = 100)
    subscriptionId = models.IntegerField()
    