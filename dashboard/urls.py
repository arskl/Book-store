from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('admin/', Admin.as_view(), name='admin'),
    path('book-create/', BookCreate.as_view(), name='book-create'),
    path('book-update/<str:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<str:pk>', BookDelete.as_view(), name='book-delete'),
    path('http-request-log/', views.httpRequestLog, name='http-request-log'),
    path('book-manipulation-log/', views.bookManipulationLog, name='book-manipulation-log'),
]
