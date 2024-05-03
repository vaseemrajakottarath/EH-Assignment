from django.db import models

# Create your models here.
GENDER_CHOICES =(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Helper(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    age = models.PositiveBigIntegerField()
    skills = models.ManyToManyField(Skill)
    assigned_customer = models.OneToOneField('Customer', related_name='helper_assignment', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField(default=0)
    adress = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    assigned_helper = models.OneToOneField(Helper, related_name='customer_assignment', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    helper = models.ForeignKey(Helper,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
