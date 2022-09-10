from django.contrib import admin
from .models import post,like,user_insta,commentPost

# Register your models here.

admin.site.register(post)
admin.site.register(like)
admin.site.register(user_insta)
admin.site.register(commentPost)