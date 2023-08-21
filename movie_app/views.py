from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.serializers import *
from movie_app.models import *
from django.shortcuts import get_object_or_404



@api_view(["GET"])
def director_list(request):
    if request.method == "GET":
        directors = Director.objects.all()
        data = DirectorSerializers(directors, many=True)
        return Response(data.data)

@api_view(["GET"])
def get_director(request, id):
    director = get_object_or_404(Director, id=id)
    serializers = DirectorSerializers(director)
    return Response(serializers.data)
