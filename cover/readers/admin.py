from django.contrib import admin
from .models import Reader, Reading
# Register your models here.
admin.site.register(Reading)
admin.site.register(Reader)