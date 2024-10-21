from django.urls import path
from . import views


urlpatterns = [
    path('incomingpallet/<str:serial_number>/', views.pallet_detail, name = 'pallet_detail')
]