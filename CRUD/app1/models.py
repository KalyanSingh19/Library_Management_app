from django.db import models

# Create your models here.
class Availability(models.TextChoices):
    AVAILABLE = 'available', 'Available'
    NOT_AVAILABLE = 'not_available', 'Not Available'

class Books(models.Model):
    reg = models.CharField(max_length=70,verbose_name='Code on Book')
    title = models.CharField(max_length=70,verbose_name='Book Title')
    issued = models.DateField(verbose_name='Issued Date')
    author = models.CharField(max_length=70,verbose_name='Authors Name')
    availability = models.CharField(max_length=15, choices=Availability.choices,default=Availability.AVAILABLE)

    def __str__(self):
        return f"{self.reg} - {self.title}"

    def get_availability_display(self):
        return self.availability.label  

