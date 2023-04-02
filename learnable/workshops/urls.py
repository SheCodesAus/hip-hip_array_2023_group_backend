from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('workshops/', views.WorkshopList.as_view()),
    path('workshops/<workshop_pk>/', views.WorkshopDetail.as_view()),
    # path('workshop-mentor/', views.WorkshopMentorsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)