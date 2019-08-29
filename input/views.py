import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from input.models import Good



def upload_file(request):
	template = 'input.html'
	promt = {
		'order': 
		'Колонки файла CSV должны иметь следующий порядок: код, наименование, уровень1, уровень2, уровень3, цена, ценаСП, количество, поля свойств, совместные покупки, единица измерения, картинка, выводить на главной, описание' 
	}
	if request.method == 'GET':
		return render(request, template , promt)
		
	csv_file = request.FILES['file']
	
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'Пожалуйста, загрузите файл формата .csv')
	
	data_set = csv_file.read().decode('cp1251') #.decode('cp1251').encode('utf-8')
	io_string = io.StringIO(data_set) 
	next(io_string)
	for colum in csv.reader(io_string, delimiter = ';'):
			created = Good.objects.update_or_create(
			code = colum[0],
			name = colum[1],
			level_1 = colum[2],
			level_2 = colum[3],
			level_3 = colum[4],
			price = colum[5],
			price_SP = colum[6],
			amount = colum[7],
			properties_field = colum[8],
			purchase = colum[9],
			unit = colum[10],
			picture = colum[11],
			output = colum[12],
			description = colum[13]
		)
	context = {}
	return render(request, template , context)
	
  
  
  
