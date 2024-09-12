from django.db import models
from django.conf import settings


class Curriculum(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el usuario
    name=models.CharField(max_length=100,null=True,verbose_name='Name')
    last_name=models.CharField(max_length=100,null=True,verbose_name='Last Name')
    about_me=models.CharField(max_length=500,null=True,verbose_name='About Me')
    email=models.EmailField(max_length=100,null=True,verbose_name='Email')
    phone=models.CharField(max_length=15,null=True,verbose_name='Phone')
    created_date=models.DateField(auto_now=True,verbose_name='Created Date')

    class Meta:
        db_table='curriculum'

    def __str__(self):
        return self.name
    
class Education(models.Model):
    curriculum=models.ForeignKey(Curriculum,on_delete=models.CASCADE,related_name='educations')
    school=models.CharField(max_length=100,null=True,verbose_name='School')
    degree=models.CharField(max_length=100,null=True,verbose_name='Degree')
    start_date=models.DateField(null=True, verbose_name='Start Date')
    end_date=models.DateField(null=True, verbose_name='End Date')
    grade=models.CharField(max_length=100,null=True,verbose_name='Grade')
    description=models.CharField(max_length=500,null=True,verbose_name='Description')

    class Meta:
        db_table='education'
        ordering=['id']

class Experience(models.Model):
    curriculum= models.ForeignKey(Curriculum,on_delete=models.CASCADE,related_name='experiences')
    title=models.CharField(max_length=100,null=True,verbose_name='Title')
    company_name=models.CharField(max_length=100,null=True,verbose_name='Company Name')
    location=models.CharField(max_length=100,null=True,verbose_name='Location')
    start_date=models.DateField(null=True, verbose_name='Start Date')
    end_date=models.DateField(null=True, verbose_name='End Date')
    description=models.CharField(max_length=500,null=True,verbose_name='Description')

    class Meta:
        db_table='experience'
        ordering=['id']