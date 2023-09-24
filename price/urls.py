from django.urls import path
# from .views import post_doctor
from .views import PostList_Price,PostDetail_Price
app_name='appprice'
urlpatterns = [
     path('price/<int:pk>/',PostDetail_Price.as_view(),name='detailcreate_price'),
     path('price/',PostList_Price.as_view(),name='listcreate_price'),
]
