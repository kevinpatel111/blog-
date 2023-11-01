from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    # path('postlist', views.postlist, name='postlist'),
    path('<slug:slug>/', views.PostDetail, name='postDetail'),
    path("logout",views.do_logout, name="logout"),
    path("",views.home, name="home")
]
