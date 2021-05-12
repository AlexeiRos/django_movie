from django.urls import path

# from . import views
from .views import (
    MoviesView,
    SerialsView,
    FilterMoviesView,
    Search,
    AddStarRating,
    JsonFilterMoviesView,
    MovieDetailView,
    SerialDetailView,
    AddReview,
    ActorView,
)

urlpatterns = [
    path("", MoviesView.as_view(), name='base'),
    path("movie/", MoviesView.as_view(), name='base'),
    path("serials/", SerialsView.as_view(), name='base'),
    path("filter/", FilterMoviesView.as_view(), name='filter'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("json-filter/", JsonFilterMoviesView.as_view(), name='json_filter'),
    path("movie/<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("serials/<slug:slug>/", SerialDetailView.as_view(), name="serial_detail"),
    path("search/", Search.as_view(), name='search'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="actor_detail"),
]