from django.contrib import admin
from ecartApp.models import QueryModel
from ecartApp.models import GenerateItem,UserRegistrationModel
# Register your models here.

admin.site.register(QueryModel)
admin.site.register(GenerateItem)
admin.site.register(UserRegistrationModel)
