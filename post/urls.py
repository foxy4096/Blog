from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:post_slug>/', views.view_post, name='post'),
    path('user/view/<int:user_id>/', views.view_user, name='user'),
    path('user/edit/', views.edit_user, name='user-edit'),
    path('create-post/', views.create_post, name='create_post'),
    path('signup/', views.signup, name='signup'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
    path('delete/', views.delete_post, name='delete'),
    path('search/', views.search, name='search')
]