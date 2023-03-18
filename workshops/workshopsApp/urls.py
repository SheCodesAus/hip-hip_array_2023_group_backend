from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('workshopsApp/', views.WorkshopList.as_view()),
    path('workshopsApp/<workshop_pk>/', views.WorkshopDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)