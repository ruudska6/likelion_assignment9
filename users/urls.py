from django.urls import path
from .views import *
from .views import profile


urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('profile/', profile, name='users-profile'),
]


