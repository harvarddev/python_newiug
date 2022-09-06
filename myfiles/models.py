from django.db import models
# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
            return self.nomi
class Kasb(models.Model):
    nomi = models.CharField(max_length=40)
    def __str__(self):
            return self.nomi

class Maxsulotlar(models.Model):
    nomi = models.CharField(max_length=40)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='media')
    tur = models.ForeignKey(Type ,on_delete=models.CASCADE,)
    vaqt = models.DateTimeField(auto_now=True)

class Projects(models.Model):
    nomi = models.CharField(max_length=40)
    manzil = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)

class Ishchilar(models.Model):
    kasb = models.ForeignKey(Kasb,on_delete=models.CASCADE)
    ism = models.CharField(max_length=40)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)




