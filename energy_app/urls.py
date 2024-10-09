from django.urls import path
from . import views
urlpatterns = [
 path('', views.energy_predict, name='energy_predict'),
]