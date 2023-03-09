from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    doj = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    empphoto = models.FileField(upload_to='empphoto')
    
    @property
    def get_photo_url(self):
        if self.empphoto and hasattr(self.empphoto,'url'):
            return self.empphoto.url
        else:
            return '/empphoto/noimg.jpg'
    
    def __str__(self):
        return str(self.empid) + ' ' + str(self.name) + ' ' + str(self.contact) + ' ' + str(self.email) + ' ' + str(self.dept) + ' ' + str(self.doj) + ' ' + str(self.dob) + ' ' + str(self.empphoto)