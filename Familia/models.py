from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre= models.CharField(max_length=128)
    fecha_nacimiento= models.DateField()
    altura=models.IntegerField()
    


class Parentezco(models.Model):
    parentezco=models.CharField(max_length=128)
    miembro=models.ForeignKey('Familiar',on_delete=models.CASCADE,null=True)