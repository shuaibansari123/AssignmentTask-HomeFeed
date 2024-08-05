from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentViewSet, ChildViewSet, BlogViewSet , BlogViewSet2

router = DefaultRouter()
router.register(r'parents', ParentViewSet)
router.register(r'children', ChildViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs-feed//<int:child_id>/' , BlogViewSet2.as_view() , name='blog-2' )
]