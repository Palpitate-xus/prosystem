# Generated by Django 3.2.9 on 2022-11-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosystem', '0002_alter_objectsquery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='field_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='classesquery',
            name='class_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='classesquery',
            name='property_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fields',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='objects',
            name='field_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='objects',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='objectsquery',
            name='field_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='objectsquery',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='objectsquery',
            name='object_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='objectsquery',
            name='property_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='field_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='querytable',
            name='class_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='querytable',
            name='object_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='querytable',
            name='property_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='querytable',
            name='relation_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
