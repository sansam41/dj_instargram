from django.urls import path
from .views import PhotoList,PhotoCreate,PhotoDelete,PhotoDetail,PhotoUpdate,PhotoLike,Photofavorite

app_name='photo'
urlpatterns=[
    path("create/",PhotoCreate.as_view(),name='create'),
    path("delete/<int:pk>",PhotoDelete.as_view(),name='delete'),
    path("update/<int:pk>",PhotoUpdate.as_view(),name='update'),
    path("detail/<int:pk>",PhotoDetail.as_view(),name='detail'),
    path("",PhotoList.as_view(),name='index'),
    path("like/<int:photo_id>/",PhotoLike.as_view(),name='like'),
    path("favorite/<int:photo_id>/",Photofavorite.as_view(),name='favorite'),
]