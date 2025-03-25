from django.contrib import admin
from django.urls import path, include
from meu_app import views

urlpatterns = [
    path('', views.page_web, name='home'),
    path('admin/', admin.site.urls),
    path('meu_app/', include('meu_app.urls')),
    path('contato/', views.contato, name='contato'),
    path('accounts/', include('accounts.urls')),
]
