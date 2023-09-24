from django.urls import path
# from .views import post_doctor
from .views import PostList_User,PostDetail_user
app_name='appuser'
urlpatterns = [
     path('detail/<int:pk>/',PostDetail_user.as_view(),name='detailcreate_reservation'),
     path('detail/',PostList_User.as_view(),name='listcreate_reservation'),
]
