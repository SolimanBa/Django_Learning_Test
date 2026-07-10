from django.urls import path
from .views import home, about, post_detail, user_posts, create_post, edit_post, delete_post, register_user, login_user, logout_user

app_name = 'blogapp'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('user/<str:username>/', user_posts, name='user_posts'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]