from django.urls import path
from . import views

urlpatterns = [
    path('smessanger/', views.SendSlackSpamMessageView.as_view(), name='smessanger'),
]