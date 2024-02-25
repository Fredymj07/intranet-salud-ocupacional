from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'update/', 
        views.UpdatePasswordView.as_view(),
        name='user-update',
    ),
]