from django.urls import path
from .views import home_view, test_form

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('test/', test_form, name='test')
]
