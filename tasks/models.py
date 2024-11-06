from django.db import models

# Create your models here.

# Aca creamos nuestras tablas que posteriormente seran generadas en db.sqlite3
# Despues de realizar el class respectivo, realizar: 
# python manage.py makemigrations --> Crea el codigo para ejecutar y crear la tabla
# python manage.py migrate --> Ejecuta el codigo y la tabla ya es creada en db.sqlite3


class Task(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title