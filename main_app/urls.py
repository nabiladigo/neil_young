from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new/',  views.ArtistCreate.as_view(), name="artist_create"),
     # Our new Route including the pk param
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    # Our new Route including the pk param
    path('artists/<int:pk>/update',views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete"),
    # path('', views.404.as_view(), name="404"),   
    path('artists/<int:pk>/songs/new/', views.SongCreate.as_view(), name="song_create")



]