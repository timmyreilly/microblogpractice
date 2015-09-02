from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "created_at"
	fields = ("published", "title", "content")
	list_display = ["published", "title", "updated_at"]
	list_display_links = ["title"]
	list_editable = ["published"]
	list_filter = ["published", "updated_at"]
		

admin.site.register(Post, PostAdmin)

