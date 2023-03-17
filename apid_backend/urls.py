from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from user import views as user_views

router = DefaultRouter()
router.register('user', user_views.UserModelViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', user_views.CustomObtainAuthToken.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
