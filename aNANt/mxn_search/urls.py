from django.urls import path

from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('',views.index,name='index'),
    path('list/',views.searchResults,name='list'),
    path(r'^details/(<pk>)',views.details,name='details'),
    #path('test/<pk>',views.testing,name='test'),
    path(r'^details/download_poscar/(<pk>)',views.download_poscar,name='download_poscar'),
    path(r'^details/download_xyz/(<pk>)',views.download_xyz,name='download_xyz'),
    path(r'^details/download_cif/(<pk>)',views.download_cif,name='download_cif'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
