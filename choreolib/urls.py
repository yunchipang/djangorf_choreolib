from django.urls import include, path
from rest_framework import routers
from choreos import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# wire up the API using automatic URL routing
# additionally, include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]