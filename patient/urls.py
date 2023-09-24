from django.urls import path
# from .views import post_doctor
from .views import PostList_patient,PostDetail_patient
app_name='appreservation'
urlpatterns = [
     path('patient/<int:pk>/',PostDetail_patient.as_view(),name='detailcreate_patient'),
     path('patient/',PostList_patient.as_view(),name='listcreate_patient'),
]
