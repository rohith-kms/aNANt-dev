from django.urls import path
import django.contrib.auth.views as auth_views

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
    path('login_page/password_reset/', auth_views.PasswordResetView.as_view(template_name = "frontpage/password_reset_form.html" , email_template_name = "frontpage/password_reset_email.html", subject_template_name = "frontpage/password_reset_subject.txt"), name='password_reset'),
    path('login_page/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'frontpage/password_reset_done.html'), name='password_reset_done'),
    path('login_page/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "frontpage/password_reset_confirm.html"), name='password_reset_confirm'),
    path('login_page/reset/done', auth_views.PasswordResetCompleteView.as_view(template_name = 'frontpage/password_reset_complete.html'), name='password_reset_complete'),
]
