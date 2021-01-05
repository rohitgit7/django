from django.conf.urls import url
from . import views

app_name = 'basicapp'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url('user_login/',views.user_login,name='user_login'),

]
