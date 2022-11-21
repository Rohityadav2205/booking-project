from django.db import models

# Create your models here.
class BookingModel(models.Model):
    Name=models.CharField(max_length=200)
    Mobile_No=models.IntegerField()
    Address =models.CharField(max_length=200)
    Age =models.IntegerField()
    Gender=models.CharField(max_length=20)
    Account_status=models.CharField(max_length=200)

def __str__(self):
    return 'Name={0},Mobile_No={1},Address={2},Age={3},Gender={4},Account={5}'.format(self.Name,self.Mobile_No,self.Address,self.Age,self.Gender,self.Account_status)



class VisitModel(models.Model):
    Mobile_No=models.IntegerField()
    Random_No=models.IntegerField()

def __str__(self):
    return "Mobile_No={0},Random_No={1}".format(self.Mobile_No,self.Random_No)