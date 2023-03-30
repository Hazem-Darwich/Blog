from django.contrib import admin
from MyApp.models import *

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)