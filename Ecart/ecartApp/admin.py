from django.contrib import admin
from ecartApp.models import Topic,Webpage,AccessRecord
from ecartApp.models import QueryModel
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(QueryModel)
