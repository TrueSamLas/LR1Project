# Generated by Django 5.0.2 on 2024-02-11 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['name'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
