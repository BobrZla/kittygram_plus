# kittygram_plus/urls.py
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')
router.register('owners', OwnerViewSet, basename='owners')
router.register(r'mycats', LightCatViewSet, basename='mycats') 


urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]