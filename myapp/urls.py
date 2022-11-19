from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'gallery', views.gallery, name='gallery'),
    path(r'gallery/add', views.addPhoto, name='addPhoto'),
    path(r'gallery/<int:pno>', views.viewPhoto, name='viewPhoto'),
    path(r'gallery/delete/<int:pno>', views.deletePhoto, name='deletePhoto'),
]