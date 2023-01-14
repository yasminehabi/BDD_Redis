from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item,home

urlpatterns = {
    path('', manage_items, name="items"),
    #path('<slug:key>', manage_item, name="single_item"),
    path('shw',home, name='Home')
}
urlpatterns = format_suffix_patterns(urlpatterns)