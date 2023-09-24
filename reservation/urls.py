from django.urls import path
# from .views import post_doctor
from .views import PostList_reservation,PostDetail_reservation
app_name='appreservation'
urlpatterns = [
     path('book/<int:pk>/',PostDetail_reservation.as_view(),name='detailcreate_reservation'),
     path('book/',PostList_reservation.as_view(),name='listcreate_reservation'),
]
