from django.contrib import admin
from .models import Bug, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Bug)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)