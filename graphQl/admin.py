from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.category)
admin.site.register(models.option)
admin.site.register(models.question)
admin.site.register(models.story)
