from django.urls import path
from .views import home_view, test_view

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('test/', test_view, name='test')
]
