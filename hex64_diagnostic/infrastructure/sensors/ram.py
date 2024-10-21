#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль SENSORS/MEMORY - отвечает за получение данных об ОЗУ. Является частью
инфраструктуры программы.

Файл: cpu.pu
Путь до файла: hex64_diagnostics/infrastructure/sensors/ram.py
"""
from typing import Dict
import psutil
from hex64_diagnostic.utils.data_convertor import convert_to_human_size


class RAMSensor:
	"""
	Класс, отвечающий за информацию о памяти
	"""
	def __init__(self):
		"""
		Инициализация
		"""
		self.svmem = psutil.virtual_memory()
		self.swap = psutil.swap_memory()

	def update_data(self):
		"""
		Обновление данных
		"""
		self.svmem = psutil.virtual_memory()
		self.swap = psutil.swap_memory()

	def get_svmem_total_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации об общем размере памяти
		"""
		return convert_to_human_size(self.svmem.total) if not in_bytes else self.svmem.total

	def get_svmem_available_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации о доступной памяти
		"""
		return convert_to_human_size(self.svmem.available) if not in_bytes else self.svmem.available

	def get_svmem_used_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации об использованной памяти
		"""
		return convert_to_human_size(self.svmem.used) if not in_bytes else self.svmem.used

	def get_svmem_percentage(self, in_bytes: bool=False) -> float:
		"""
		Метод получения информации о проценте памяти
		"""
		return self.svmem.percent

	def get_svmem_cached_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации о кешированной памяти
		"""
		return convert_to_human_size(self.svmem.cached) if not in_bytes else self.svmem.cached

	def get_svmem_shared_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации о shared памяти
		"""
		return convert_to_human_size(self.svmem.shared) if not in_bytes else self.svmem.shared

	def get_swap_total_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации об общем размере swap
		"""
		return convert_to_human_size(self.swap.total) if not in_bytes else self.swap.total

	def get_swap_used_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации об использованном размере swap
		"""
		return convert_to_human_size(self.swap.used) if not in_bytes else self.swap.used

	def get_swap_sin_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации о SIN swap
		"""
		return convert_to_human_size(self.swap.sin) if not in_bytes else self.swap.sin

	def get_swap_sout_size(self, in_bytes: bool=False) -> str:
		"""
		Метод получения информации о SOUT swap
		"""
		return convert_to_human_size(self.swap.sout) if not in_bytes else self.swap.sout

	def get_swap_percentage(self, in_bytes: bool=False) -> float:
		"""
		Метод получения информации о проценте swap
		"""
		return self.swap.percent

	def get_full_info(self, in_bytes: bool=False) -> Dict[str, str | float]:
		"""
		Метод получения всей информации о памяти

		:return: словарь с данными
		:rtype: Dict[str, str | float]
		"""
		self.update_data()

		result = {
			'svmem_total_size': self.get_svmem_total_size(),
			'svmem_available_size': self.get_svmem_available_size(),
			'svmem_used_size': self.get_svmem_used_size(),
			'svmem_percentage': self.get_svmem_percentage(),
			'svmem_cached_size': self.get_svmem_cached_size(),
			'svmem_shared_size': self.get_svmem_shared_size(),

			'swap_total_size': self.get_swap_total_size(),
			'swap_used_size': self.get_swap_used_size(),
			'swap_percentage': self.get_swap_percentage(),
			'swap_sin_size': self.get_swap_sin_size(),
			'swap_sout_size': self.get_swap_sout_size(),
		}

		return result
