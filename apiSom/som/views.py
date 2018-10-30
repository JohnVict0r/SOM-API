from django.shortcuts import render

from django.http import HttpResponse

import ColorSom


def index(request):
	colorSom=ColorSensorSOM()
	colorSom.lerFile()
	colorSom.train()
	teste_vermelho=[45, 156, 115]
	colorSom.winner(teste_vermelho)

	return HttpResponse(colorSom)

# Create your views here.
