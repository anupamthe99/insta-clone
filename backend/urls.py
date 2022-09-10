from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    # path('',views.commentPost,name="comment"),
    path('upload',views.upload,name="upload"),
    path('like',views.like_post,name="like"),
    path('profile/<str:pk>',views.profile,name="profile"),
    path('edit/<slug:slug>',views.edit,name="edit"),
    path('search',views.search_username,name="search"),
    # path('search-profile',views.search_profile,name="search-profle"),
    path('profile-info',views.profile_info,name="profile-info"),
    path('commentPost/<slug:slug>',views.commentPostapi,name="commentPost"),
    # path('comment/<slug:slug>',views.comment,name="comment"),
]
