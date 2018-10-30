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
		self.DATA_URL = self.DOWNLOAD_ROOT + self.DATA_PATH + self.FILE_TO_DOWNLOAD
		self.fetch_data()

	def fetch_data(data_url=self.DATA_URL, data_path=self.DATA_PATH, file_to_download=self.FILE_TO_DOWNLOAD):
		if not os.path.isdir(data_path):
			os.makedirs(data_path)
		urllib.request.urlretrieve(data_url, data_path+file_to_download)

	def lerFile():
		leitura = csv.reader(open('master/'+śelf.FILE_TO_DOWNLOAD,'r'))
		leitura = list(leitura) # tem que converter pra lista primeiro
		leitura = np.array(leitura)# e depois converte pra array
		self.objetos_coloridos = leitura [1:,0:3] # objeto vermelho é o array apenas numérico
		self.objetos_coloridos = self.objetos_coloridos.astype(float)

	def train():

		colors=self.objetos_coloridos 
		self.som = MiniSom(x = 25, y = 25, input_len = 3, sigma = 1.0, learning_rate = 0.5)
		self.som.random_weights_init(colors)
		self.som.train_random(data = colors, num_iteration = 100)

	def winner(test):
		result=self.som.winner(test)
		return result