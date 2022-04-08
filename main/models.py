from django.db import models
from datetime import date, datetime
from django.urls import reverse


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_age(self):
        age = date.today().year - self.birth_date.year
        return age



class Employee(AbstractPerson):
    work_position = models.CharField(max_length=30)
    experience = models.DateField()

    def __str__(self):
        return self.work_position
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('employee_detail', kwargs={'pk': self.id})


class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    card_id = models.CharField(max_length=10)

    def __str__(self):
        return self.employee
    
    def save(self, *args, **kwargs):
        print(f'{self.employee.name} has been saved!')
        super().save(*args, **kwargs)




class WorkProject(models.Model):
    project_name = models.CharField(max_length=15)
    members = models.ManyToManyField(Employee, through="Membership")

    def __str__(self):
        return self.project_name

class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return self.employee

class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.address
    
class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def __str__(self):
        return self.vip_status_start