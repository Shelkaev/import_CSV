from django.db import models

# Create your models here.


class Level_1(models.Model):
	level_1 = models.CharField(null=True, blank=True, max_length=50)
	def __str__(self):
		return self.level_1

class Level_2(models.Model):
	level_2 = models.CharField(null=True, blank=True, max_length=50)
	def __str__(self):
		return self.level_2
		
class Level_3(models.Model):
	level_3 = models.CharField(null=True, blank=True, max_length=50)
	def __str__(self):
		return self.level_3
		


class Good(models.Model):
	code = models.CharField(verbose_name='Код', max_length=10, null=True, blank=True)
	
	name = models.CharField(verbose_name='Наименование', max_length=50, null=True, blank=True)
	
	level_1 = models.ForeignKey(
	'Level_1', on_delete=models.CASCADE, null=True, verbose_name='Уровень1'
	)
	
	level_2 = models.ForeignKey(
	'Level_2', on_delete=models.CASCADE, null=True, verbose_name='Уровень2'
	)
	
	level_3 = models.ForeignKey(
	'Level_3', on_delete=models.CASCADE, null=True, verbose_name='Уровень3'
	)
	
	price = models.DecimalField(
	verbose_name='Цена', max_digits=6, decimal_places=2, null=True, blank=True
	)
	
	price_SP = models.DecimalField(
	verbose_name='ЦенаСП', max_digits=6,decimal_places=2, null=True, blank=True
	)
	
	amount = models.FloatField(
	verbose_name='Количество', null=True, blank=True
	)
		
	properties_field = models.CharField(
	verbose_name='Поля свойств', max_length=255, null=True, blank=True
	)
	
	purchase = models.FloatField(
	verbose_name='Совместные покупки', null=True, blank=True
	)
	
	unit = models.CharField(
	verbose_name='Единица измерения', max_length=15, null=True, blank=True
	)
	
	picture = models.CharField(verbose_name='Картинка', null=True, blank=True, max_length=50)
	
	output = models.BooleanField(verbose_name='Выводить на главной')
	
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	
	def __str__(self):
		return self.name