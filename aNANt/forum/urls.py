from django.urls import path

from . import views

urlpatterns = [
	path('',views.forum,name='forum'),
	path('make_post/',views.make_post,name='make_post'),
	path('posts/<int:pk>/',views.view_post,name='view_post'),
	path('posts/<int:pk>/make_comment/',views.make_comment,name='make_comment'),

	]
