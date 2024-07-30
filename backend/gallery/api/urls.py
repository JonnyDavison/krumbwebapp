from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet

gallery_router = DefaultRouter()
gallery_router.register(r'gallery', GalleryViewSet)