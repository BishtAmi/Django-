from django.db import models

# Create your models here.
'''
Register type- student / prof
name -
college_id -
department - 
'''
class UserInfo(models.Model):
    type= models.CharField(max_length=10)
    name= models.CharField(max_length=20)
    college_id= models.CharField(max_length=15,unique=True)
    department=models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"


class Financial(models.Model):
    college_id= models.CharField(max_length=15, unique=True)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    fees = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'financial_info'
