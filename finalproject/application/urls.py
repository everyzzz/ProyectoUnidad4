from django.urls import path
from application import views

urlpatterns = [
        path('', views.Index.as_view(), name="index"),
        path('form/', views.Form.as_view(), name="form")
]