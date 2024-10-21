#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль SENSORS/CPU - отвечает за получение данных о температуре комплектющих. Является частью
инфраструктуры программы.

Файл: temp.pu
Путь до файла: hex64_diagnostics/infrastructure/sensors/temp.py
"""
from typing import List, Dict
import platform
import psutil
from hex64_diagnostic.utils.other import print_msg


class TempSensor:
	"""
	Класс, реализующий получение информации с сенсоров температур
	"""
	def __init__(self):
		"""
		Инициализация класса и его свойств
		"""
		if platform.system() != "Linux":
			print_msg(f'Ваша ОС не поддерживается сенсорами температуры вентиляторов. Ваша ОС: {platform.system()}', 'warning')
		elif platform.system() == 'Linux':
			self.funs_dict = psutil.sensors_fans()

		self.temps_dict = psutil.sensors_temperatures()

	def update_data(self):
		if platform.system() != "Linux":
			print_msg(f'Ваша ОС не поддерживается сенсорами температуры вентиляторов. Ваша ОС: {platform.system()}', 'warning')
		elif platform.system() == 'Linux':
			self.funs_dict = psutil.sensors_fans()

		self.temps_dict = psutil.sensors_temperatures()

	def get_cpu_temp(self) -> int:
		"""
		Метод для получения температуры процессора.

		.. warning: данный метод, к сожалению, пока не работает на Windows

		:return: температура процессора
		"""
		if platform.system() != "Linux":
			# TODO: реализовать получение температуры процессора на Windows
			return "n/a"

		with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
			return int(str(file.read())[:2])

	def update_temps(self):
		"""
		Метод обновления сенсоров
		"""
		self.temps_dict = psutil.sensors_temperatures()
		self.funs_dict = psutil.sensors_fans()

	def get_temperature_sensors(self) -> List[str]:
		"""
		Метод для получения температур сенсоров

		:return: список со всеми температурами
		:rtype: List[str]
		"""
		sensors = []

		for temp_sensor, temp_info in self.temps_dict.items():
			sensors.append(temp_info[0].current)

		return sensors

	def get_temperature_sensors_with_names(self) -> List[List]:
		"""
		Метод для получения температур сенсоров с именами

		:return: список со всеми температурами
		:rtype: List[str]
		"""
		sensors = []

		for temp_sensor, temp_info in self.temps_dict.items():
			sensors.append([temp_sensor, temp_info[0].current, temp_info[0].high, temp_info[0].critical])

		return sensors

	def get_current_temp_by_name(self, temp_sensor_name: str) -> float:
		"""
		Метод получения текущей температуры по имени сенсора

		:param temp_sensor_name: название сенсора
		:type: str

		:return: текущая температура
		:rtype: float
		"""
		try:
			return self.temps_dict[temp_sensor_name][0].current
		except KeyError:
			return 0.0

	def get_high_temp_by_name(self, temp_sensor_name: str) -> float:
		"""
		Метод получения высокого порога температуры по имени сенсора

		:param temp_sensor_name: название сенсора
		:type: str

		:return: высокий порог температуры
		:rtype: float
		"""
		try:
			return self.temps_dict[temp_sensor_name][0].high
		except KeyError:
			return 0.0

	def get_critical_temp_by_name(self, temp_sensor_name: str) -> float:
		"""
		Метод получения критической температуры по имени сенсора

		:param temp_sensor_name: название сенсора
		:type: str

		:return: критическая температура
		:rtype: float
		"""
		try:
			return self.temps_dict[temp_sensor_name][0].critical
		except KeyError:
			return 0.0

	def get_info_by_name(self, temp_sensor_name: str) -> Dict[str, float | None]:
		"""
		Метод для получения полной информации о температуре по имени сенсора температуры.
		
		:param temp_sensor_name: название сенсора
		:type: str

		:return: список с данными
		:rtype: Dict[str, float | None]
		"""
		sensor_info = {
			'current': self.get_current_temp_by_name(temp_sensor_name),
			'high': self.get_high_temp_by_name(temp_sensor_name),
			'critical': self.get_critical_temp_by_name(temp_sensor_name)
		}

		return sensor_info

	def get_full_info(self) -> Dict[str, str | None | float]:
		"""
		Получение полной возможной информации о температуре

		:return: список с данными о температурах
		:rtype: Dict[str, str | None | float]
		"""
		result = {
			'cpu_temp': self.get_cpu_temp(),
			'temps': self.get_temperature_sensors(),
		}

		for key, value in self.temps_dict.items():
			result[key] = {
				'info': self.get_info_by_name(key),
				'value': value
			}

		return result
