from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminType(admin. ModelAdmin):
    list_display = ['id','nomi']
admin. site.register(Type, AdminType)

class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(Maxsulotlar,AdminMax)


class AdminPro(admin.ModelAdmin):
    list_display = ['id','nomi','manzil','rasm','vaqt']
admin.site.register(Projects,AdminPro)


class AdminIsh(admin.ModelAdmin):
    list_display = ['id','kasb','malumot','rasm','vaqt']
admin.site.register(Ishchilar,AdminIsh)


class AdminKasb(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Kasb,AdminKasb)