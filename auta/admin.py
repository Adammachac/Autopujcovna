# admin.py
from django.contrib import admin
from .models import Zakaznik, Auto

admin.site.register(Auto)
admin.site.register(Zakaznik)
