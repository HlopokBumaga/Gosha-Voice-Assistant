#Gosha revision: 3_0g21_0
#Модули:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Распознание голоса
import speech_recognition as sr
#Голос бота
import pyttsx3
#Время
from datetime import datetime
#Погода
from pyowm import OWM
#Переводчик
from translate import Translator
#Рандом для некоторых функций
import random
#Время
import time as t
#Файл с рисунком
import Ascii
#Работа с файлами
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
#Музыка
import pygame as pg
#Progress Bar
from tqdm import tqdm
#Выход
from sys import exit
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pg.mixer.init()

#Голос, НЕ ТРОГАТЬ(ЕСЛИ НЕ РАЗБИРАЕШЬСЯ)!!!----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Aleksandr':
        engine.setProperty('voice', voice.id)

#Список действий и другое...------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Список комманд
help_list = "Время\nПомощь\nПогода\nЗавершить работу\nДокументация\nУправление файлами\nШутки\nПереводчик\nСписок микрофонов"

#Список комманд для файлов
help_file = "1)Создать файл или папку\n2)Переименовать файл или папку\n3)Записать в файл\n4)Прочитать файл\n5)Удалить файл или папку\n6)Узнать директорию\n7)Сменить директорию"

#Шутки
joke1 = ["Я не знаю шуток! ха-ха!",  "Знаешь почему курица перешла дорогу? Потому что она умеет ходить! ха-ха!", "Россия - страна непойманных воров и вечно будущего счастья...", "Если вдоль зебры лежат полицейские, значит, охота не удалась.","Детство - это когда кот старше тебя.","Идея тонкого комплимента: 'Маска тебе к лицу!'","Очень боюсь, что хакеры сольют в сеть мои интимные фото. И они никому не понравятся."]

#Словарь обращений
appeal = {"помощь": ["помощь", "помоги мне", "список команд", "что ты умеешь"],
		  "время": ["время", "который час", "сколько времени", "назови время"],
		  "завершить работу": ["завершить работу", "увидимся"],
		  "документация": ["документация", "покажи документацию", "у тебя есть инструкция", "где версии"],
		  "управление файлами": ["управление файлами", "файлы", "я бог файлов"],
		  "шутки": ["шутки", "расскажи шутку", "ты знаешь шутку"],
		  "погода": ["погода", "какая погода", "прогноз погоды"],
		  "переводчик": ["переводчик", "переведи мне", "можешь перевести"],
          "выключение компьютера": ["выключи компьютер", "выключение", "выключение компьютера"],
		  "список микрофонов": ["список микрофонов", "микрофоны"]
}

#Пасхалки
pasx_list = ["pasx.wav","pasx2.wav","pasx3.wav","pasx4.wav"]

#Список микрофонов
type_micr = sr.Microphone.list_microphone_names()

#Микрофона
with open("Settings.py", "r") as st:
    line = st.read()

micr = int(line[26:27])

st.close

#Основные функции------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Говорение
def speak(what):
    print( what )
    engine.say( what )
    engine.runAndWait()
    engine.stop()

#Шутки
def joke():
	ask_joke = random.choice(joke1)
	speak(ask_joke)
	joke_pl = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + "\\Data_Gosha\\Music\\Joke_Gosha\\joke.wav")
	joke_pl.play()
	t.sleep(3)

#Помощь
def help():
	speak("Список комманд: ")
	speak(help_list)

#Время
def time():
	now = datetime.now()
	speak("Сейчас: " + str(now.hour) + ":" + str(now.minute))

#Пасхалки
def pasx():
	for i in tqdm(range(100)):
		t.sleep(0.01)
	print(Ascii.pasx_image)
	asd = random.choice(pasx_list)
	pasx = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + f"\\Data_Gosha\\Music\\Pasx_Gosha\\{asd}")
	pasx.play()
	gh = input()
	if gh == "stop":
		pasx.stop()

def pacx2():
	for i in tqdm(range(100)):
		t.sleep(0.01)
	print(Ascii.pacx_image2)
	pasx2a = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + f"\\Data_Gosha\\Music\\Pasx_Gosha\\Pasxan.wav")
	pasx2a.play()
	gh2 = input()
	if gh2 == "stop":
		pasx2a.stop()

#Документация
def doc():
	speak("Открытие...")
	for i in tqdm(range(100)):
		t.sleep(0.01)
	t.sleep(1)
	os.startfile(os.path.dirname(os.path.abspath(__file__)) + "\\Gosha_Doc.chm")

#Переводчик
def transletor():
	speak("Напиши что хочешь перевести: ")
	trn = input()
	speak("Введи язык твоей написанной фразы: ")
	from_l = input()
	speak("Введи язык перевода: ")
	to_l = input()
	translator= Translator(from_lang = from_l, to_lang = to_l)
	translation = translator.translate(trn)
	
	for i in tqdm(range(100)):
		t.sleep(0.01)
	
	speak("Переведённая фраза звучит так: " + translation)

#Погода
def weather_jk():
	try:
		owm = OWM('599651a6555d21da39a6b27988381476')
		speak("Напиши название города: ")
		place = input()
		
		monitoring = owm.weather_manager().weather_at_place(place)
		weather = monitoring.weather
		status = weather.detailed_status
		temperature = weather.temperature('celsius')['temp']
		
		translator2 = Translator(from_lang = "English", to_lang = "Russian")
		status2 = translator2.translate(status)
		
		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak("Сейчас в городе температура: " + str(temperature) + "°С ")
		speak(status2)
	
	except:
		speak("Такого города не существует!")

#Функции для работы с файлами-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Управление файлами
def file_meneger():	
	print(help_file)
	help_file_quest = input()
	if help_file_quest == "1)":
		new_file()
	elif help_file_quest == "2)":
		rename()
	elif help_file_quest == "3)":
		write()
	elif help_file_quest == "4)":
		read()
	elif help_file_quest == "5)":
		delet()
	elif help_file_quest == "6)":
		dir_qu()
	elif help_file_quest == "7)":
		dir_gg()
	else:
		speak("Я в своём познании совсем преисполнился!")

#Новый файл или папка
def new_file():
	speak("Ты хочешь создать файл или папку? ")
	type_gg = input()
	if type_gg == "Файл":
		speak("Предупреждение! Файл будет создан в той директории, где вы сейчас! ")
		speak("Напиши название файла: ")
		name21 = input()
		open(name21, "w")

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak(f"Создан файл {name21}, в директории " + os.getcwd() + " !")
	elif type_gg == "Папка":
		speak("Предупреждение! Папка будет создана в той директории, где вы сейчас! ")
		speak("Напиши название папки: ")
		name213 = input()
		os.mkdir(name213)

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak(f"Создана папка под именем {name213}, в директории " + os.getcwd() + " !")
	else:
		speak("Я в своём познании совсем преисполнился!")

#Переименовать файл или папку
def rename():
	try:
		speak("Предупреждение! Что-бы переименовать файл или папку нужно быть в той-же директории, где находится файл! ")
		speak("Введи старое имя файла или папки: ")
		name211 = input()
		speak("Введи новое имя файла или папки: ")
		name_new = input()
		os.rename(name211, name_new)

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak(f"Переименован файл или папка под новым именем {name_new}, в директории " + os.getcwd() + " !")
	
	except FileNotFoundError:
		speak("Я не нашёл такого файла или папки!")

#Записать в файл
def write():
	try:
		speak("Предупреждение! Что-бы записать что-то в файл нужно быть в той-же директории, где находится файл! ")
		speak("Введи имя файла: ")
		name_file = input()
		speak("Введи то что хочешь записать в файл: ")
		wrote = input()
		file = open(name_file, "w")
		file.write(wrote)

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak(f"Было записанно {wrote}, в файл под именем {name_file}, в директории " + os.getcwd() + " !")

	except FileNotFoundError:
		speak("Не найден файл для записи!")

#Прочитать файл
def read():
	try:
		speak("Предупреждение! Что-бы прочитать файл нужно быть в той-же директории, где находится файл! ")
		speak("Извини конечно, но я не много тупой и не понимаю Руский язык! По этому лучше дай мне почитать Английский язык!")
		speak("Введи имя файла: ")
		read_file = input()
		file_ff = open(read_file, "r")

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak(file_ff.read())

	except FileNotFoundError:
		speak("Не найден файл для чтения!")

#Удалить файл или папку
def delet():
	try:
		speak("Что ты хочешь удалить? Файл или папку? ")
		fg = input()
		if fg == "Файл":
			speak("Предупреждение! Что-бы удалить файл нужно быть в той-же директории, где находится файл! ")
			speak("Какой файл ты хочешь удалить? ")
			delet_file = input()
			os.remove(delet_file)

			for i in tqdm(range(100)):
				t.sleep(0.01)

			speak(f"Был удален файл с именем {delet_file}, в директории " + os.getcwd() + " !")
		elif fg == "Папка":
			speak("Предупреждение! Что-бы удалить папку нужно быть в той-же директории, где находится папка! ")
			speak("Какую папку ты хочешь удалить? ")
			delet_file = input()
			os.rmdir(delet_file)

			for i in tqdm(range(100)):
				t.sleep(0.01)

			speak(f"Была удалена папка с именем {delet_file}, в директории " + os.getcwd() + " !")
		else:
			speak("Я в своём познании совсем преисполнился!")

	except FileNotFoundError:
		speak("Не найден файл или папка для удаления!")

#Узнать директорию
def dir_qu():
	for i in tqdm(range(100)):
		t.sleep(0.01)
	speak("Текущая деректория: " + os.getcwd())

#Сменить директорию
def dir_gg():
	try:
		speak("Куда ты хочешь перейти? ")
		dir_gg = input()
		os.chdir(dir_gg)

		for i in tqdm(range(100)):
			t.sleep(0.01)

		speak("Текущая директория изменилась на: " + os.getcwd())
	
	except FileNotFoundError:
		speak("Данной директории не существует!")

#Приветствие-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(Ascii.start)

for i in tqdm(range(100)):
    t.sleep(0.01)

speak("Здравствуй! Тебя приветствует голосовой помощник Gosha!")
speak("Жду твоих указаний:")

#Основной цикл-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = True
while run:
	try:
		r = sr.Recognizer()
		try:
			with sr.Microphone(device_index=micr) as source:
				print("Слушаю...")
				audio = r.listen(source)
		
		except:
			speak("Извините, но без микрофона я не могу работать!")
			exit()

		what = r.recognize_google(audio, language = "ru-RU").lower()
		print(what)

		#Помощь
		if what in appeal["помощь"]:
			help()
		
		#Время
		elif what in appeal["время"]:
			time()

		#Выйти
		elif what in appeal["завершить работу"]:
			speak("До встречи!")
			run = False
		
		#Шутка
		elif what in appeal["шутки"]:
			joke()

		#Пасхалки
		elif what == "1987":
			pasx()

		elif what == "пять невест":
			pacx2()

		#Управление файлами
		elif what in appeal["управление файлами"]:
			speak("Что ты хочешь сделать?")
			file_meneger()

		#Документация
		elif what in appeal["документация"]:
			doc()

		#Погода
		elif what in appeal["погода"]:
			weather_jk()
		
		#Переводчик
		elif what in appeal["переводчик"]:
			transletor()
		
		#Автор
		elif what == "автор":
			speak("Мой автор отбитый на голову человек! Но я всё равно ему благодарен за создание меня! Мой автор: DimaK")

		#Выключение компьютера
		elif what in appeal["выключение компьютера"]:
			speak("Предупреждение! Выключение произойдёт через 5 секунд!")
			t.sleep(5)
			os.system("shutdown /s")
		
		#Список микрофонов
		elif what in appeal["список микрофонов"]:
			for i in tqdm(range(100)):
				t.sleep(0.01)
			
			for i in range(len(type_micr)):
				print(i, type_micr[i])

		#Ни одна комманда не сработала
		else:
			speak("Извини! Такой комманды не существует!")

	except sr.UnknownValueError:
		speak("Я тебя не слышу! Повторите попытку!")
	except sr.RequestError:
		speak("Плохое соеденение с интернетом:(")
		exit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Автор: DimaK