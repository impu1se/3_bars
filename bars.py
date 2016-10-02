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
	fix_coordinate = []
	for coordinate in list_bars:
		x2, y2 = coordinate['Cells']['geoData']['coordinates']
		res = (x+y)-(x2+y2)
		if res < 0:
			res = res*-1
		fix_coordinate.append(res)				 
	return min(fix_coordinate)
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

