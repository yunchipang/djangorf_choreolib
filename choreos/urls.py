from django.urls import path
from choreos import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('choreos/', views.ChoreographyList.as_view()),
    path('choreos/<int:pk>/', views.ChoreographyDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)