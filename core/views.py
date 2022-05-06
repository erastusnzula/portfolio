from django.shortcuts import render, redirect
from django.views import View

from core.forms import CommentForm, ContactForm
from core.models import Project, Comment, Category, Contact, DownloadFiles, Setting


class HomePage(View):
    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        settings = Setting.objects.all()
        context = {
            'projects': projects,
            'settings': settings,
        }
        return render(self.request, 'core/home_page.html', context)


class ProjectDetails(View):
    def get(self, request, id, title):
        project = Project.objects.get(id=id, title=title)
        form = CommentForm()
        comments = Comment.objects.filter(project=project).order_by('-added_on')
        settings = Setting.objects.all()
        context = {
            'project': project,
            'form': form,
            'comments': comments,
            'settings': settings,
        }
        return render(self.request, 'core/project_details.html', context)

    def post(self, request, id, title):
        project = Project.objects.get(id=id, title=title)
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            content = form.cleaned_data.get('content')
            comment = Comment()
            comment.username = username
            comment.content = content
            comment.project = project
            comment.save()
            return redirect('core:project-details', id=id, title=title)


class ProjectCategory(View):
    def get(self, request, category, *args, **kwargs):
        projects = Project.objects.filter(category__name__contains=category)
        settings = Setting.objects.all()
        context = {
            'projects': projects,
            'category': category,
            'settings': settings,
        }
        return render(self.request, 'core/category.html', context)


class ContactMe(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, 'core/contact.html', context)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            Contact(
                email=email,
                message=message
            ).save()
            return redirect('core:contact')


class Download(View):
    def get(self, *args, **kwargs):
        files = DownloadFiles.objects.all()
        settings = Setting.objects.all()
        context = {
            'files': files,
            'settings': settings,
        }
        return render(self.request, 'core/download.html', context)


class Settings(View):
    def get(self, *args, **kwargs):
        settings = Setting.objects.all()
        context = {
            'settings': settings
        }
        return render(self.request, 'core/settings.html', context)


def get_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context
