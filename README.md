# Поиск баров.
Это программа которая показывает самый большой и маленький бар в г.Москве, а так же по указанным координатам определяет самый близкий бар. 
# Необходимые файлы
Для этого вам необходимо скачать файл с портала открытых данных в формате json.
Скачать файл можно по [ссылке](http://data.mos.ru/opendata/export/1796/json/2/1)  
# Работа с программой
Запускается скрипт с указанием в качестве первого **параметра** название и путь до файла в кавычках с указанием *расширения*. После запуска программы будет выведено меню выбора:  
1.  Самый большой   
2.  Самый маленький бар  
3.  Определить ближайший бар по координатам  
4.  Выход из программы  
Для определения наиближайшего к вам по расстоянию бара - узнайте ваши точные координаты широты и долготы, и укажите их при выборе пунтка № 3.
Данные программы будут выведенны на экран.  

**Пример запуска программы:** `python bars.py 'filename.json'`
# Возможные ошибки
В случае не правильного ввода названия файла или в случае его отсутствии программа прекращает работу.
