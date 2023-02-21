from django.urls import path
from choreos import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('choreos/', views.choreographies_list),
    path('choreos/<int:pk>/', views.choreography_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)