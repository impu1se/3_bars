import sys
import json

def open_file(file_bars):
	try:
		with open(file_bars, encoding='utf-8') as f:
			return json.load(f)
	except FileNotFoundError:
		print('Файл не найден')
		sys.exit(1)

def list_max_bars(list_bars):
	max_bars = []
	seats = [bar['Cells']['SeatsCount'] for bar in list_bars]
	for bar in list_bars:
		if bar['Cells']['SeatsCount'] == max(seats):
				max_bars.append(bar['Cells']['Name'])
	return max_bars

def list_min_bars(list_bars):
	min_bars = []
	seats = [bar['Cells']['SeatsCount'] for bar in list_bars]
	for bar in list_bars:
		if bar['Cells']['SeatsCount'] == min(seats):
			min_bars.append(bar['Cells']['Name'])
	return min_bars

def find_bars(list_bars, x, y):
	bar_dict = {}
	for bar in list_bars:
		name_bar = bar['Cells']['Name']
		x2,y2 = bar['Cells']['geoData']['coordinates']
		bar_dict.update({name_bar:(x2+y2)})
	
					 
	return bar_dict
#123

if __name__ == '__main__':
	list_bars = open_file(sys.argv[1])
	while True:
		answer = input("Что вы хотите узнать?: \n1 - Самые большие бары \
						\n2 - Самые маленькие бары \n3 - Узнать бар по координатам \
						\n4 - Выход из программы \nВведите номер: ")
		if answer == '1':
			print(list_max_bars(list_bars))
		elif answer == '2':
			print(list_min_bars(list_bars))
		elif answer == '3':
			x = int(input("Введите ваши координаты по оси x: "))
			y = int(input("Введите ваши координаты по оси y: "))
			print(find_bars(list_bars,x,y))
		elif answer == '4':
			sys.exit()
		else :
			print("Не правильный ввод\n\n")

