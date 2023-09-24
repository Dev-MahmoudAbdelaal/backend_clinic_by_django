from django.urls import path
# from .views import post_doctor
from .views import PostList_Address,PostDetail_Address
app_name='appAddress'
urlpatterns = [
     path('address/<int:pk>/',PostDetail_Address.as_view(),name='detailcreate_Address'),
     path('address/',PostList_Address.as_view(),name='listcreate_Address'),
]
