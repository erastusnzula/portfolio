from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('contact/', views.ContactMe.as_view(), name='contact'),
    path('download/', views.Download.as_view(), name='downloads'),
    path('settings/', views.Settings.as_view(), name='settings'),
    path('<category>/', views.ProjectCategory.as_view(), name='category'),
    path('<id>/<title>/', views.ProjectDetails.as_view(), name='project-details'),

]
