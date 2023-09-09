from django.contrib import admin

from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
'''from django.contrib import admin

from .models import Room

admin.site.register(Room)'''