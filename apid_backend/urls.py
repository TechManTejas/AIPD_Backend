from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user import views as user_views
from doctor import views as doctor_views
from patient import views as patient_views
from condition import views as condition_views
from exercise import views as exercise_views

router = DefaultRouter()
router.register('user', user_views.UserModelViewSet, basename='user')
router.register('doctor', doctor_views.DoctorModelViewset, basename='doctor')
router.register('patient', patient_views.PatientModelViewset, basename='patient')
router.register('condition', condition_views.ConditionModelViewset, basename='condition')
router.register('exercise', exercise_views.ExerciseModelViewset, basename='exercise')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', user_views.CustomObtainAuthToken.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
