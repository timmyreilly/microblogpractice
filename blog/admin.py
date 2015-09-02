from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "created_at"

admin.site.register(Post, PostAdmin)

