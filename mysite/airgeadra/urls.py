from django.urls import path
from . import views
app_name = 'airgeadra'
urlpatterns = [
  #  path('your_url/', views.your_view, name='your_view_name'),
path('', views.index, name='index'),
]
