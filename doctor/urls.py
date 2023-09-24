from django.urls import path
# from .views import post_doctor
from .views import PostList_Doctor,PostDetail_Doctor
app_name='appdoctor'
urlpatterns = [
     path('doctor/<int:pk>/',PostDetail_Doctor.as_view(),name='detailcreate_doctor'),
     path('doctor/',PostList_Doctor.as_view(),name='listcreate_doctor'),
]
