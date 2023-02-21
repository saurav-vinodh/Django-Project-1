from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="Developer Saurav"
admin.site.site_title="Welcome to Harry's Dashboard"
admin.site.index_title="Welcome to this portal" 

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact,name='contact'),
    path('project',views.project,name='project'),
    ]