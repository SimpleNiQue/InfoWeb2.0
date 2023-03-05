from .views import index, login, registration
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration')
]