from .views import index, login, RegistrationView, CustomLoginView
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login2/', CustomLoginView.as_view(), name='login2'),
]