#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль SENSORS/CPU - отвечает за получение данных о процессоре. Является частью
инфраструктуры программы.

Файл: cpu.pu
Путь до файла: hex64_diagnostics/infrastructure/sensors/cpu.py
"""
import os
import re
import subprocess
import psutil
import platform
from typing import Dict, List
from cpuinfo import get_cpu_info
from hex64_diagnostic.utils.data_convertor import convert_to_human_size


class CPUSensor:
	"""
	Класс, представляющий собой сенсор CPU. Данный класс собирает всю информацию о процессоре.
	"""
	def __init__(self):
		"""
		Инициализация класса
		"""
		self.uname_info = platform.uname()
		self.processor_name = self._detect_processor_name()
		self.cpu_info = get_cpu_info()

	def update_data(self):
		self.uname_info = platform.uname()
		self.processor_name = self._detect_processor_name()
		self.cpu_info = get_cpu_info()

	def _detect_processor_name(self):
		"""
		Скрытый метод для определения названия процессора в зависимости от ОС. Поддерживаются Windows, Linux и MacOS

		:rtype: str
		:return: название процессора
		"""
		if platform.system() == "Windows":
			return platform.processor()
		elif platform.system() == "Darwin":
			os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
			command = "sysctl -n machdep.cpu.brand_string"

			return subprocess.check_output(command).strip()
		elif platform.system() == "Linux":
			command = "cat /proc/cpuinfo"
			command_output = subprocess.check_output(command, shell=True).decode().strip()

			for line in command_output.split("\n"):
				if "model name" in line:
					return re.sub(".*model name.*:", "", line, 1).replace('Processor', '').strip()

		return "N/A Model"

	@property
	def uname_processor(self):
		"""
		Свойство класса для получения полного имени процессора
		"""
		return f'{self.processor_name} {self.uname_info.machine}'

	def get_cores_count(self, logical: bool=True) -> int:
		"""
		Функция для получения количества ядер.

		:param logical: учитывать ли логические ядра
		:type: bool

		:return: число ядер в процессоре
		:rtype: int
		"""
		return int(psutil.cpu_count(logical=logical))

	def get_cpu_frequency(self) -> Dict[str, float]:
		"""
		Метод для получения частоты процессора

		:return: словарь с максимальной, минимальной и текущей частотой процессора
		:rtype: Dict[str, str]
		"""
		cpufreq = psutil.cpu_freq()

		max_freq = round(cpufreq.max, 2)
		min_freq = round(cpufreq.min, 2)
		curr_freq = round(cpufreq.current, 2)

		return {
			'max': max_freq,
			'min': min_freq,
			'current': curr_freq,
		}

	def get_cpu_usage_percentage_per_core(self) -> List[float]:
		"""
		Метод получения процента использования на каждое ядро процессора.

		:return: список процента использования ядер
		:rtype: List[float]
		"""
		core_usage_percentages = []

		for _, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
			core_usage_percentages.append(percentage)

		return core_usage_percentages

	def get_total_cpu_usage_percentage(self) -> int:
		"""
		Метод получения процента использования процессора

		:return: процент использования ЦП
		:rtype: int
		"""
		return int(psutil.cpu_percent())

	def get_cpu_times_percent(self) -> Dict[str, float]:
		"""
		Метод получения процента использования каждого из объектов (user,
		nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice).

		:return: словарь с процентами использования
		:rtype: Dict[str, float]
		"""
		cpu_percentage = {}
		result = psutil.cpu_times_percent(interval=1, percpu=False)

		cpu_percentage = {
			'user': result.user,
			'nice': result.nice,
			'system': result.system,
			'idle': result.idle,
			'iowait': result.iowait,
			'irq': result.irq,
			'softirq': result.softirq,
			'steal': result.steal,
			'guest': result.guest,
			'guest_nice': result.guest_nice
		}

		return cpu_percentage

	def get_statistics(self) -> Dict[str, int]:
		"""
		Метод получения статистики процессора (прерывания, свитчи ctx, системные вызовы).

		:return: словарь со статистикой
		:rtype: Dict[str, int]
		"""
		cpu_stat = psutil.cpu_stats()

		result = {
			'ctx_switches': cpu_stat.ctx_switches,
			'interrupts': cpu_stat.interrupts,
			'soft_interrupts': cpu_stat.soft_interrupts,
			'syscalls': cpu_stat.syscalls
		}

		return result

	def get_load_average_percentage(self) -> List[float]:
		"""
		Метод получения средней загруженности процессора.

		:return: список из трех значений
		:rtype: List[float]
		"""
		return [round(x / psutil.cpu_count() * 100, 2) for x in psutil.getloadavg()]

	def get_full_info(self) -> Dict[str, str | dict | list | int | float]:
		"""
		Функция получения всей полной информации о процессоре в виде словаря.

		:return: словарь со всеми данными
		:rtype: Dict[str, str | dict | list | int | float]
		"""
		processor_info = {
			'processor': self.processor_name,
			'total_cores_count': self.get_cores_count(True),
			'physical_cores_count': self.get_cores_count(False),
			'cpu_frequency': self.get_cpu_frequency(),
			'cores_usage_percentage': self.get_cpu_usage_percentage_per_core(),
			'cpu_usage_percentage': self.get_total_cpu_usage_percentage(),
			'cpu_times_percent': self.get_cpu_times_percent(),
			'cpu_load_average': self.get_load_average_percentage(),
			'cpu_statistics': self.get_statistics(),
			'architecture': self.cpu_info['arch'],
			'bits': self.cpu_info['bits'],
			'vendor_id_raw': self.cpu_info['vendor_id_raw'],
			'brand_raw': self.cpu_info['brand_raw'],
			'hz_advertised_friendly': self.cpu_info['hz_advertised_friendly'],
			'hz_actual_friendly': self.cpu_info['hz_actual_friendly'],
			'model': self.cpu_info['model'],
			'family': self.cpu_info['family'],
			'flags': self.cpu_info['flags'],
			'l3_cache_size': convert_to_human_size(self.cpu_info['l3_cache_size']),
			'l2_cache_size': convert_to_human_size(self.cpu_info['l2_cache_size']),
			'l1_data_cache_size': convert_to_human_size(self.cpu_info['l1_data_cache_size']),
			'l1_instruction_cache_size': convert_to_human_size(self.cpu_info['l1_instruction_cache_size']),
			'l2_cache_line_size': convert_to_human_size(self.cpu_info['l2_cache_line_size']),
			'l2_cache_associativity': convert_to_human_size(self.cpu_info['l2_cache_associativity']),
		}

		return processor_info
