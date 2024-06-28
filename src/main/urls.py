from django.urls import path
from .views import main_view, home_view
from . import views

urlpatterns = [
    path('', main_view, name= 'main'),
    path('home/', home_view, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/update/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
]
