from django.urls import path
from reg_app.views import registration_page, user_login

urlpatterns = [
    path('', registration_page),
    path('login/', user_login)
]
