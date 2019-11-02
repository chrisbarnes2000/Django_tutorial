from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:event_id>/', views.detail, name='detail'),
]