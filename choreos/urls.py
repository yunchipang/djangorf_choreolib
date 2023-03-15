from django.urls import path, include
from rest_framework.routers import DefaultRouter
from choreos import views

# create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"choreos", views.ChoreographyViewSet, basename="choreography")
router.register(r"users", views.UserViewSet, basename="user")

# the API urls are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user, name='register'),
]
