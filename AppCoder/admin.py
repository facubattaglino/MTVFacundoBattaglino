from django.contrib import admin
from AppCoder.models import familia
# Register your models here.
class familiaresAdmin(admin.ModelAdmin):

    list_display = ('nombre','apellido','edad','fecha_nacimiento','profesion')
admin.site.register(familia, familiaresAdmin)