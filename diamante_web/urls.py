
from django.contrib import admin
from django.urls import path, include
from meu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_web, name='home'),
    path('meu_app/', include('meu_app.urls')),
]
