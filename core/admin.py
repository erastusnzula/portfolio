from django.contrib import admin
from core.models import Project, Category, Comment, Contact, DownloadFiles, Setting

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(DownloadFiles)
admin.site.register(Setting)
