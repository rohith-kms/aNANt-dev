from django.urls import path

from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('result/',views.creepResults,name='creepresult'),
]

urlpatterns += staticfiles_urlpatterns()
