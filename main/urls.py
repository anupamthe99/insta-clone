from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from authentication import views as auth_view
from django.urls import re_path as url

import authentication
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("backend.urls")),
    path('login',auth_view.user_login,name="login"),
    url('signup', auth_view.signup, name='signup'),
    url('logout', auth_view.signout, name='logout'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
