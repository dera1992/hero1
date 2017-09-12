from django.conf.urls import url

from ku import views

urlpatterns = [
   url(r'^$', views.home, name ='home'),

]
