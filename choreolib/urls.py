from django.urls import path, include

urlpatterns = [
    path('', include('choreos.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]