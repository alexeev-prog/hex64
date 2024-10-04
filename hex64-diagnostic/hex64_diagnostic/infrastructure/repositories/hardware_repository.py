#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль REPOSITORIES/HARDWARE_REPOSITORY - отвечает за хранение и использование данных с
сенсоров. Является частью инфраструктуры программы.

Файл: hardware_repository.pu
Путь до файла: hex64_diagnostics/infrastructure/repositories/hardware_repository.py
"""
from hex64_diagnostic.infrastructure.sensors.cpu import CPUSensor
from hex64_diagnostic.infrastructure.sensors.ram import RAMSensor
from hex64_diagnostic.infrastructure.sensors.temp import TempSensor
from hex64_diagnostic.infrastructure.sensors.disk import DiskSensor
from hex64_diagnostic.infrastructure.sensors.network import NetworkSensor
from typing import Dict


class HardwareDataManager:
	def __init__(self, cpu_data: 'CPUSensor', ram_data: 'RAMSensor', temp_data: 'TempSensor', 
					disk_data: 'DiskSensor', network_data: 'NetworkSensor'):
		self.cpu_data = cpu_data
		self.ram_data = ram_data
		self.temp_data = temp_data
		self.disk_data = disk_data
		self.network_data = network_data

		self.merged_data = {
			'cpu': self.cpu_data.get_full_info(),
			'ram': self.ram_data.get_full_info(),
			'temp': self.temp_data.get_full_info(),
			'disk': self.disk_data.get_full_info(),
			'network': self.network_data.get_full_info()
		}

	def update_data(self):
		self.cpu_data.update_data()
		self.ram_data.update_data()
		self.temp_data.update_data()
		self.disk_data.update_data()
		self.network_data.update_data()

		self.merged_data = {
			'cpu': self.cpu_data.get_full_info(),
			'ram': self.ram_data.get_full_info(),
			'temp': self.temp_data.get_full_info(),
			'disk': self.disk_data.get_full_info(),
			'network': self.network_data.get_full_info()
		}

	def get_cpu_info(self) -> Dict[str, str | dict | int | list | float]:
		return self.merged_data['cpu']

	def get_ram_info(self) -> Dict[str, str | dict | int | list | float]:
		return self.merged_data['ram']

	def get_temp_info(self) -> Dict[str, str | dict | int | list | float]:
		return self.merged_data['temp']

	def get_disk_info(self) -> Dict[str, str | dict | int | list | float]:
		return self.merged_data['disk']

	def get_network_info(self) -> Dict[str, str | dict | int | list | float]:
		return self.merged_data['network']

	def get_full_info(self) -> Dict[str, dict]:
		return self.merged_data
