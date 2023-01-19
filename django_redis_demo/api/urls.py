from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import home,action,home_view

urlpatterns = {


    path('shw',home, name='Home'),
    path('action',action, name='action'),
    #path('show',show, name='show'),
   path('home_view',home_view, name='home_view')
}
urlpatterns = format_suffix_patterns(urlpatterns)