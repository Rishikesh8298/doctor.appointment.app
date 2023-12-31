from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100, db_column="specialty", unique=True)

    def __str__(self):
        return self.name
