from django.contrib import admin
from .models import Emoloyee, Role, Department


# Register your models here.

admin.site.register(Emoloyee)
admin.site.register(Role)
admin.site.register(Department)

