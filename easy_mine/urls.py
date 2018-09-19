from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('release/', views.upload_file, name='upload_file'),
    path('release/move', views.movefile, name='movefile'),
    path('add/', views.TicketCreateView.as_view(), name='ticket_add'),
    path('', views.TicketListView.as_view(), name='home'),
    path('<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
]
