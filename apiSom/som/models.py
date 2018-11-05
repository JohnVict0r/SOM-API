from django.db import models


class Caracteristicas(models.Model):

	text_red_field = models.IntegerField();
	text_green_field = models.IntegerField();
	text_blue_field = models.IntegerField();

