from django.urls import path
# from .views import post_doctor
from .views import PostList_consulation,PostDetail_consulation
app_name='appconsulation'
urlpatterns = [
     path('consulation/<int:pk>/',PostDetail_consulation.as_view(),name='detailcreate_consulation'),
     path('consulation/',PostList_consulation.as_view(),name='listcreate_consulation'),
]
