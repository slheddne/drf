# Imports -> Django
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Imports -> Quickstart -> Views
from quickstart import views

# Routers -> Default router to register the viewsets
router = routers.DefaultRouter()

# Routers -> Register the viewsets
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'songs', views.SongViewSet)

urlpatterns = [
    # Endpoints -> Admin
    path('admin/', admin.site.urls),

    # Endpoints -> API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# URLS -> Add the router urls
urlpatterns += router.urls
