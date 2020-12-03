from django.urls import path
from .views import PhotoList,PhotoCreate,PhotoDelete,PhotoDetail,PhotoUpdate,PhotoLike,\
    Photofavorite,PhotoFavoriteList,PhotoLikeList,PhotoMyList

app_name='photo'
urlpatterns=[
    path("create/",PhotoCreate.as_view(),name='create'),
    path("delete/<int:pk>",PhotoDelete.as_view(),name='delete'),
    path("update/<int:pk>",PhotoUpdate.as_view(),name='update'),
    path("detail/<int:pk>",PhotoDetail.as_view(),name='detail'),
    path("",PhotoList.as_view(),name='index'),
    path("like/<int:photo_id>/",PhotoLike.as_view(),name='like'),
    path("favorite/<int:photo_id>/",Photofavorite.as_view(),name='favorite'),
    path("like/",PhotoLikeList.as_view(),name='like_list'),
    path("favorite/",PhotoFavoriteList.as_view(),name='favorite_list'),
    path("mylist/",PhotoMyList.as_view(),name='mylist'),
]