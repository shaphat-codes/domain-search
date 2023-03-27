
from django.contrib import admin
from django.urls import path
from scraper import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('name-cheap/', views.NameCheap, name='post'),
    path('domain/', views.Domain, name='post'),
    path('hover/', views.Hover, name='post')
]
