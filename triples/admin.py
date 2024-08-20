from django.contrib import admin
from .models import Triples

@admin.register(Triples)
class TriplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity1', 'relationship', 'entity2')
