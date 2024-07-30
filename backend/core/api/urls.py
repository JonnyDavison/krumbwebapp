from rest_framework.routers import DefaultRouter
from gallery.api.urls import gallery_router
from django.urls import path, include

router = DefaultRouter()
# Gallery
router.registry.extend(gallery_router.registry)

urlpatterns = [
    path('', include(router.urls))
]