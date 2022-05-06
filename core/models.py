import readtime
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name='projects', default='Python')
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/projects', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    github = models.CharField(max_length=255, default='', null=True, blank=True)
    live = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def get_read_time(self):
        return readtime.of_text(self.description)


class Comment(models.Model):
    username = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(verbose_name='Comment')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    email = models.EmailField(verbose_name='Enter your email address')
    message = models.TextField(verbose_name='Enter message')


class DownloadFiles(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads/mobile/%Y/%m/%d/', null=True, blank=True)
    windows = models.FileField(upload_to='downloads/windows/%Y/%m/%d/', default='', null=True, blank=True)
    linux = models.FileField(upload_to='downloads/linux/%Y/%m/%d/', default='', null=True, blank=True)
    description = models.TextField(default='', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about[:20] + '...'
