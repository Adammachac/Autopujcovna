from django.db import models

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Auto(models.Model):
    model = models.CharField(max_length=100)
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True, blank=True)
    rok_vyroby = models.IntegerField(default=2020)  # <--- nové pole
    dostupne = models.BooleanField(default=True)

    def __str__(self):
        return self.model
