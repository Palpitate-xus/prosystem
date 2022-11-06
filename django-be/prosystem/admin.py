import imp
from operator import mod
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Classes)
admin.site.register(ClassesQuery)
admin.site.register(Fields)
admin.site.register(Objects)
admin.site.register(ObjectsQuery)
admin.site.register(Properties)
admin.site.register(QueryTable)
