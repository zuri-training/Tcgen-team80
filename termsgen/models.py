from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class database(models.Model):
    Company_name = models.CharField(max_length = 23, null=True)
    email_Address = models.CharField(max_length = 23 , null=True)
    phone_number = models.CharField(max_length = 23,  null=True)
    fax_number = models.CharField(max_length=23, null=True)
    Address = models.CharField(max_length=23, null=True)
    country = models.CharField(max_length=23, null=True)
    state_province_or_teritory = models.CharField(max_length=23, null=True)
    city = models.CharField(max_length = 23, null=True)
    zip_or_postal_code = models.CharField(max_length = 23, null=True)
    


    def __str__(self):
        return self.Company_name


class signUp(models.Model):
    email_Address = models.EmailField()
    password = models.CharField(max_length=8, null=True)


    # def_str_(self):
    # return self.e