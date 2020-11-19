from django.urls import path

from . import views

urlpatterns = [
    path('', views.applicationsview, name='applications'),
    path('add', views.addrequest, name='add'),
    path('<int:pk>/', views.RequestDetailView.as_view(), name='applications-detail'),
    path('<int:pk>/update/', views.RequestUpdateView.as_view(), name='applications-update'),
    path('<int:pk>/delete/', views.RequestDeleteView.as_view(), name='applications-delete'),

]
