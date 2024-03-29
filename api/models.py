from django.db import models

class Bucketlist(models.Model):
    #bucketlist model
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __self__(self):
        #Return a human readable representation of the model instance.
        return "{}".format(self.name)

