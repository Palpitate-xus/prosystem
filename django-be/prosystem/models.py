# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classes(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    field_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classes'


class ClassesQuery(models.Model):
    class_id = models.IntegerField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classes_query'


class Fields(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    field = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fields'


class Objects(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    object = models.TextField(blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'objects'


class ObjectsQuery(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'objects_query'


class Properties(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    info = models.TextField(blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'properties'


class QueryTable(models.Model):
    object_id = models.IntegerField(blank=True, null=True)
    relation_id = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'query_table'
