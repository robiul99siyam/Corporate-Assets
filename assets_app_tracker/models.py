from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone



""" this is company model """

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.company_name


""" This is the deviece model """

class Device(models.Model):
    
    company = models.ForeignKey(Company,on_delete=models.CASCADE, blank=True,null=True,related_name='company')

    device_name = models.CharField(max_length=100)

    deviec_sarial_number = models.IntegerField()

    deviec_type = models.CharField(max_length=100)

    device_description = models.TextField()

    device_condition = models.CharField(max_length=150 , default="GOOD")

  

    def __str__(self):
        return self.device_name + "  to  " + self.company.company_name





"""this is the emplayee model here"""

class Employee(models.Model):

    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)

    device = models.ManyToManyField(Device)

    employee_name = models.CharField(max_length=100)

    employee_email = models.EmailField()

    employee_current_address = models.CharField(max_length=100)

    employee_parmanent_address = models.CharField(max_length=100)

    employee_phone_number = models.CharField(max_length=18)

    employee_national_id_number =  models.CharField(max_length=18)

    employee_department_name = models.CharField(max_length=100)

    employee_parchased_data = models.DateTimeField(default=timezone.now)

    employee_return_data = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.employee_name

   




""" this is assets return model here """


class AssetsReturn (models.Model):

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True,related_name = "employee")

    device = models.ForeignKey(Device,on_delete=models.CASCADE,blank=True,null=True,related_name='device')

    return_date = models.DateTimeField(default=timezone.now)

    return_condition = models.TextField()


    def __str__(self):
        return f"{self.employee.employee_name } to {self.device.device_name}"

    
     