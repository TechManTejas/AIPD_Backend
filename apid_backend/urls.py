from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

from user import views as user_views
from doctor import views as doctor_views
from fittlyf_physio import views as fittlyf_physio_views
from patient import views as patient_views
from condition import views as condition_views
from exercise import views as exercise_views
from exerciserecord import views as exercise_records_views
from patient_exercise import views as patient_exercise_views

router = DefaultRouter()
router.register('user', user_views.UserModelViewSet, basename='user')
router.register('doctor', doctor_views.DoctorViewSet, basename='doctor')
router.register('fittlyf_physio', fittlyf_physio_views.FittlyfPhysioViewSet, basename='fittlyf_physio')
router.register('patient', patient_views.PatientViewSet, basename='patient')
router.register('condition', condition_views.ConditionViewSet,
                basename='condition')
router.register('exercise', exercise_views.ExerciseViewSet,
                basename='exercise')
router.register('exercise_record',
                exercise_records_views.ExerciseRecordViewSet, basename='exercise_record')
router.register('exercise_record_redundant',
                exercise_records_views.RedundantExerciseRecordViewSet, basename='exercise_record_redundant')
router.register('patient_exercise',
                patient_exercise_views.PatientExerciseViewSet, basename='patient_exercise')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', user_views.CustomObtainAuthToken.as_view()),
    path('get-aws-server-data/', views.git_push_view, name='get-aws-server-data'),
    path('update-aws-server/', views.git_pull_view, name='update-aws-server'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
