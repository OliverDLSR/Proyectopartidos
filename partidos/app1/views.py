from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PartidoPolitico
from .serializers import PartidoPoliticoSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Página de inicio")


class ListaPartidos(APIView):
    def get(self, request):
        partidos = PartidoPolitico.objects.all()
        serializer = PartidoPoliticoSerializer(partidos, many=True)
        return Response(serializer.data)



def partidos_view(request):
    return render(request, 'paginas/partidos.html')