from django.db import models
from django.urls import reverse


# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    # The absolute path to get the url then reverse into 'employeep_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('employee_edit', kwargs={'pk': self.pk})