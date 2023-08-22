from django.urls import path, include
from rest_framework import routers

from rest_quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"s", views.SnippetViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]
