from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, logout_then_login


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(),  name='register'),
    path('logout/',logout_then_login, name='logout'),
]