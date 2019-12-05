from django.conf.urls import url
from . import views
# from .models import Shows

                    
urlpatterns = [
     url(r'^lor$', views.lor),
     url(r'^regpro$', views.reg_pro),
     url(r'^success$', views.success),
     url(r'^logpro$', views.log_pro)
]