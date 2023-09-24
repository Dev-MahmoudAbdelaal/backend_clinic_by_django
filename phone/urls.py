from django.urls import path
# from .views import post_doctor
from .views import PostList_phone,PostDetail_phone
app_name='appphone'
urlpatterns = [
     path('phone/<int:pk>/',PostDetail_phone.as_view(),name='detailcreate_phone'),
     path('phone/',PostList_phone.as_view(),name='listcreate_phone'),
]
