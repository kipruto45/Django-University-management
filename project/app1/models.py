from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum


class RoleChoices(Enum):
    ADMIN = 'Admin'
    PROF = 'Profesor'
    STUDENT = 'Student'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class StatusChoices(Enum):
    PRI = 'Prijavljen'
    POL = 'Položen'
    PAD = 'Izgubljen potpis'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
    

class StatusStudentsChoices(Enum):
    NONE = 'None'
    IZVANREDNI = 'Izvanredni'
    REDOVNI = 'Redovni'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class Uloge(models.Model):
    role = models.CharField(max_length=20, choices=RoleChoices.choices())

    def __str__(self):
        return self.role


class StatusStudenta(models.Model):
    status = models.CharField(max_length=30, choices=StatusStudentsChoices.choices())

    def __str__(self):
        return self.status


class Status(models.Model):
    status = models.CharField(max_length=30, choices=StatusChoices.choices())

    def __str__(self):
        return self.status


class Korisnik(AbstractUser):
    role = models.ForeignKey(Uloge, on_delete=models.CASCADE, blank="true", null="true")
    status = models.ForeignKey(StatusStudenta, on_delete=models.CASCADE, blank="true", null="true")


class Predmeti(models.Model):
    name = models.CharField(max_length=30)
    kod = models.CharField(max_length=10)
    program = models.TextField()
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=3)
    nositelj = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank="true", null="true")

    def __str__(self):
        return self.name

class Korisnik_Predmet(models.Model):
    korisnik = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank=True, null=True)
    predmeti = models.ForeignKey(Predmeti, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True, default=1)