from django.db import models

class Category(models.Model):
    name = models.CharField("Список", max_length=150)
    description = models.TextField("Названия", max_length= 1000)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
