from django.urls import path, include
# from .views import movie_list, movie_detail
from .views import ReviewCreate,  ReviewList, ReviewDetail, StreamPlateformVS, StreamPlateformDetailAV, WatchDetailAV, WatchListAV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlateformVS, basename='streamplateform')

urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(), name='movie-detail'),
    # path('stream/', StreamPlateformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlateformDetailAV.as_view(), name='stream-detail')

    path('', include(router.urls)),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    
    
   # path('reviews/<str:username>', UserReview.as_view(), name="user-review")
]