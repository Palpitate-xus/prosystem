# Generated by Django 3.2.16 on 2022-10-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectsquery',
            name='id',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
    ]
