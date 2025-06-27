from django.urls import path

from .views import custLoginView, custLogoutView, register

urlpatterns = [
    path("login/", custLoginView, name="login"),
    path("logout/", custLogoutView, name="logout"),
    path('register/', register, name='register')
]

