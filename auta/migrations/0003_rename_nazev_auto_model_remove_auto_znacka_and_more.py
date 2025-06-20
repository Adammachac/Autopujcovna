# Generated by Django 5.1.7 on 2025-04-08 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auta', '0002_auto_remove_zakaznik_email_remove_zakaznik_telefon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='nazev',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='znacka',
        ),
        migrations.RemoveField(
            model_name='zakaznik',
            name='auto',
        ),
        migrations.AddField(
            model_name='auto',
            name='dostupne',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='zakaznik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auta.zakaznik'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='rok_vyroby',
            field=models.IntegerField(default=2020),
        ),
    ]
