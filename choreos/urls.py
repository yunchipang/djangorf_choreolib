from django.urls import path
from choreos import views

urlpatterns = [
    path('choreos/', views.choreographies_list),
    path('choreos/<int:pk>/', views.choreography_detail),
]