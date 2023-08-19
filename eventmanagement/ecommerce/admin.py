from django.contrib import admin

# Register your models here.
from .models import Customer, Comment

admin.site.register(Customer)
admin.site.register(Comment)