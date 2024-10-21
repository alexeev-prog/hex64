#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль UTILS/other - вспомогательная часть кода, нужна только для сторонних функций.

Файл: other.pu
Путь до файла: hex64_diagnostics/utils/other.py
"""
from datetime import datetime
from rich import print


def get_current_datetime(underscores=False) -> str:
	"""
	Функция получения текущей даты и времени

	:return: дата и время в формате YY-MM-DD HH:MM:SS
	:rtype: str
	"""
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S') if not underscores else datetime.now().strftime('%Y-%m-%d_%H:%M:%S')


def print_msg(msg_text: str, msg_type: str) -> str:
	"""
	Функция для вывода сообщения с красивым форматированием

	:param msg_text: текст сообщения
	:type str
	:param msg_type: тип сообщения
	:type str

	:return: сообщение с форматированием и датой
	:rtype: str
	"""
	msg_type = msg_type.upper()

	if msg_type == 'INFO':
		return f'[dim]{get_current_datetime()}[/dim] [green][{msg_type}][/green] {msg_text}'
	elif msg_type == 'WARNING':
		return f'[dim]{get_current_datetime()}[/dim] [yellow][{msg_type}][/yellow] {msg_text}'
	elif msg_type == 'ERROR':
		return f'[dim]{get_current_datetime()}[/dim] [red][{msg_type}][/red] {msg_text}'
	elif msg_type == 'DEBUG':
		return f'[dim]{get_current_datetime()}[/dim] [blue][{msg_type}][/blue] {msg_text}'
	else:
		return f'[dim]{get_current_datetime()}[/dim] [cyan][{msg_type}][/cyan] {msg_text}'


def credits():
	"""
	Функция для вывода информации о проекте
	"""
	print('-' * len('  / // / __/ |/_/ / __// / /         PC Monitoring, Analysing, Diagnostic Toolkit'))
	print('''[white]   __ _______  __  ____ ____         [/white][blue]hex64 Diagnostic v0.15.18[/blue]
[white]  / // / __/ |/_/ / __// / /         [/white][dim]PC Monitoring, Analysing, Diagnostic Toolkit[/dim]
[white] / _  / _/_>  <  / _ \\/_  _/        [/white] [dim]developed by alxvdev[/dim]
[white]/_//_/___/_/|_|  \\___/ /_/          [/white] [cyan]https://github.com/alxvdev/hex64[/cyan]''')
	print('-' * len('  / // / __/ |/_/ / __// / /         PC Monitoring, Analysing, Diagnostic Toolkit'))
	print()


def versions_history():
	"""
	Функция вывода истории версий
	"""
	history = '''
0.1.0 - base architecture
0.1.1 - base utils
0.1.2 - cpu sensor
0.2.2 - ram sensor
0.2.3 - benchmark module architecture
0.3.3 - temp sensor
0.4.3 - disk sensor
0.5.3 - cpu single/multi benchmark
0.6.3 - create hardware repository
0.6.4 - fix bugs, fix docstrings
0.7.4 - create benchmark repository
0.7.5 - fixing bugs in benchmarks, improve multi benchmark
0.7.6 - improve hardware repository and fix bugs
0.7.7 - replace settings by constants in config module (and add basic constants)
0.7.8 - improve utils module, fix bugs
0.7.9 - improve docs
0.7.10 - improve cpu sensor, fix data convertor
0.8.10 - add network sensor
0.8.11 - improve disk sensor
0.8.12 - fix docstrings, fix small bugs
0.9.12 - add plots_generator with plots module
0.9.13 - add disk plot generator in plots module
0.9.14 - improve docs and docstrings
0.10.14 - create domain entities zone (hardware)
0.10.15 - create GUI App colorscheme
0.10.16 - create base gui ui template
0.10.17 - improve gui (cpu info)
0.11.17 - improve gui (cpu info tab done)
0.12.17 - improve gui (ram info tab done)
0.13.17 - improve gui (disk info tab done)
0.14.17 - improve gui (temp info tab done)
0.15.17 - improve gui (network info tab done)
0.15.18 - small bugfix and small changes in gui (information tab is done)
	'''
	print(history)
