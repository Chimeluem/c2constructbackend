from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=255)
    processed = models.BooleanField(default=False)
    info = models.TextField(max_length=500, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name)

class Qualifications(models.Model):
    first_aider = models.CharField(max_length=100)
    cscs_card = models.CharField(max_length=100)
    Fire_Marshall = models.CharField(max_length=100)
    driving_license = models.CharField(max_length=100)

    def __str__(self):
        return F"{self.first_aider} of {self.cscs_card} or  {self.Fire_Marshall}"

class Job(models.Model):
    firstName = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    phoneNumber = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=255)
    processed = models.BooleanField(default=False)
    first_aider = models.BooleanField(default=False)
    cscs_card = models.BooleanField(default=False)
    Fire_Marshall = models.BooleanField(default=False)
    driving_license = models.BooleanField(default=False)
    licenseType = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=500, blank=False, null=False)
    city = models.CharField(max_length=500, blank=False, null=False)
    country = models.CharField(max_length=500, blank=False, null=False)
    zipCode = models.CharField(max_length=500, blank=False, null=False)
    address1 = models.CharField(max_length=500, blank=False, null=False)
    address2 = models.CharField(max_length=500, blank=True, null=True)
    additionalInfo = models.TextField(max_length=500, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class SiteDetail(models.Model):
    phone = models.CharField(max_length=100)
    address = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.phone)