from django.db import models
from django.utils import timezone
import uuid
import datetime

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

''' Un evento esta compuesto de nombre,  una  categoría  (las  cuatro  posibles 
categorías  son:  Conferencia,  Seminario,  Congreso  o  Curso
),  un  lugar,  una  dirección, una  fecha  de 
inicio y una fecha de fin, y si el evento es presencial o virtual '''
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    method = models.BooleanField('is virtual')

    def __str__(self):
        return self.name


