from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('delete/<int:pk>', views.UserDelete.as_view(), name='user-delete'),
    
]
