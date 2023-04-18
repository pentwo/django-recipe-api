"""
URLs mapping for the recipe APIs
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register("recipe", views.RecipeViewSet)  # register the viewset
router.register("tag", views.TagViewSet)

app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
