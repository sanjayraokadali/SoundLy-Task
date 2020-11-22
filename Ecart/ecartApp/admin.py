from django.contrib import admin
from ecartApp.models import QueryModel
from ecartApp.models import GenerateItem
from ecartApp.models import Cart
# Register your models here.

admin.site.register(QueryModel)
admin.site.register(GenerateItem)
admin.site.register(Cart)
