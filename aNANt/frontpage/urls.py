from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('publications/',views.publications,name='publications'),
    path('acknowledgements/',views.acknowledgements,name='acknowledgements'),
    path('login_page/', views.login_page, name = 'login_page'),
    path('login_page/login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('login_page/register/', views.register, name = 'register'),
]
