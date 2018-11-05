from django.shortcuts import render

from django.http import HttpResponse





# Create your views here.
import os
import tarfile
from six.moves import urllib
import csv
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class ColorSensorSOM(object):
	def __init__(self, FILE_TO_DOWNLOAD="objetosECores.csv", DOWNLOAD_ROOT="https://raw.githubusercontent.com/rodolfostark/ColorSensorMachineLearning/", DATA_PATH="master/"):
		super(ColorSensorSOM, self).__init__()
		self.FILE_TO_DOWNLOAD=FILE_TO_DOWNLOAD
		self.DOWNLOAD_ROOT=DOWNLOAD_ROOT
		self.DATA_PATH=DATA_PATH
		self.DATA_URL=self.DOWNLOAD_ROOT+self.DATA_PATH+self.FILE_TO_DOWNLOAD
		self.fetch_data(self.DATA_URL, self.DATA_PATH, self.FILE_TO_DOWNLOAD)
	def fetch_data(self, data_url, data_path, file_to_download):
		if not os.path.isdir(data_path):
			os.makedirs(data_path)
		urllib.request.urlretrieve(data_url, data_path+file_to_download)

	def lerFile(self):
		leitura=csv.reader(open('master/'+self.FILE_TO_DOWNLOAD,'r'))
		leitura=list(leitura) # tem que converter pra lista primeiro
		leitura=np.array(leitura)# e depois converte pra array
		self.objetos_coloridos=leitura [1:,0:3] # objeto vermelho é o array apenas numérico
		self.objetos_coloridos=self.objetos_coloridos.astype(float)

	def train(self):
		colors=self.objetos_coloridos 
		self.som=MiniSom(x=25, y=25, input_len=3, sigma=1.0, learning_rate=0.4)
		self.som.random_weights_init(colors)
		self.som.train_random(data=colors, num_iteration=100)

	def winner(self, test):
		result=self.som.winner(test)
		return result

def index(request):
	colorSom=ColorSensorSOM()
	colorSom.lerFile()
	colorSom.train()
	teste_vermelho=[45, 156, 115]
	result=colorSom.winner(teste_vermelho)

	resposta="{"+'A: {0}, B: {1} '.format(result[0], result[1])+"}"

	return HttpResponse(resposta)
