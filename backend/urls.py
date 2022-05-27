from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('upload',views.upload,name="upload"),
    path('like',views.like_post,name="like"),
    path('profile/<str:pk>',views.profile,name="profile"),
    path('edit',views.edit,name="edit"),
    path('search',views.search_username,name="search"),
    path('search-profile',views.search_profile,name="search-profle"),
    path('profile-info',views.profile_info,name="profile-info"),
]
