from django.contrib import admin
from .models import *
from users.models import User
from users.models import Profile
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Profile)