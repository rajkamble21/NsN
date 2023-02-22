from django.contrib import admin
from .models import Client, Artist, Work

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'first_name', 'last_name', 'email']

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email


# class WorkInline(admin.TabularInline):
#     model = Artist.works.through
#     extra = 1
#     verbose_name_plural = 'Works'
#     fields = ('link',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'works_link', 'works_link_type']
    # inlines = [WorkInline]

    def works_link(self, obj):
        return ", ".join([work.link for work in obj.works.all()])

    works_link.short_description = 'Link'

    def works_link_type(self, obj):
        return ", ".join([work.link_type for work in obj.works.all()])

    works_link_type.short_description = 'Link Type'
    

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'link_type']
