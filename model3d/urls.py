from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^model/user/list/$', views.user_model_list, name='user_model_list'),
    url(r'^model/user/$', views.upload_model, name='upload_model'),
]