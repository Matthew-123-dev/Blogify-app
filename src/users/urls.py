from django.urls import path
from .views import login_view, register_view, logout_view, profile, profile_detail_view, profile_update


urlpatterns=[
    path('login/', login_view, name= 'login' ),
    path('register/', register_view, name= 'register'),
    path('logout/', logout_view, name= 'logout' ),
    path('profile/', profile, name='profile'),
    path('profile/<slug:slug>/', profile_detail_view, name='profile-detail'),
]