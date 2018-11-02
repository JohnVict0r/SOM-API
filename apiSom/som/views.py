from django.shortcuts import render

from django.http import HttpResponse

from ColorSom import SOM


def index(request):
	colorSom=ColorSensorSOM()
	colorSom.lerFile()
	colorSom.train()
	teste_vermelho=[45, 156, 115]
	colorSom.winner(teste_vermelho)
	return HttpResponse(colorSom)

# Create your views here.
