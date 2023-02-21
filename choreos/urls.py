from django.urls import path
from choreos import views
from rest_framework.urlpatterns import format_suffix_patterns

# API endpoints
urlpatterns = [
    path('', views.api_root),
    path('choreos/', views.ChoreographyList.as_view(), name="choreography-list"),
    path('choreos/<int:pk>/', views.ChoreographyDetail.as_view(), name="choreography-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)