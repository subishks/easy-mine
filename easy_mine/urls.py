from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('release/', views.upload_file, name='upload_file'),
    path('release/move', views.movefile, name='movefile'),
]
