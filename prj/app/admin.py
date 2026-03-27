from django.contrib import admin
from .models import User, Settings, Taktika, Kategorie


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "minecraft_username", "role")
    search_fields = ("name", "minecraft_username")
    list_filter = ("role",)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__name",)


@admin.register(Kategorie)
class KategorieAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Taktika)
class TaktikaAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty", "effectivity", "usefulness", "category", "author")
    list_filter = ("category", "difficulty")
    search_fields = ("name", "author__name")
