from django.urls import path

from movie_app import views
from movie_app.views import *


urlpatterns = [
    path("api/v1/directors/", views.director_list),
    path("api/v1/directors/<int:id>/", views.get_director),

]