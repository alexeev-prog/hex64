#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль SENSORS/DISK - отвечает за получение данных о дисках и его разделе. Является частью
инфраструктуры программы.

Файл: disk.pu
Путь до файла: hex64_diagnostics/infrastructure/sensors/disk.py
"""
from typing import Dict, List
import psutil
from diskinfo import Disk, DiskInfo
from hex64_diagnostic.utils.data_convertor import convert_to_human_size


class DiskSensor:
	"""
	Класс, полачающий информацию о дисках и разделах
	"""
	def __init__(self):
		"""
		Инициализация базовых объектов
		"""
		self.partitions = psutil.disk_partitions(all=True)
		self.di = DiskInfo()
		self.disks = self.di.get_disk_list(sorting=True)

	def update_data(self):
		self.partitions = psutil.disk_partitions(all=True)
		self.di = DiskInfo()
		self.disks = self.di.get_disk_list(sorting=True)

	def get_disks_paths(self) -> List[str]:
		"""
		Метод для получения путей дисков

		:return: Список путей
		:rtype: List[str]
		"""
		result = []

		for disk in self.disks:
			result.append(disk.get_path())

		return result

	def get_full_disk_info(self) -> Dict[str, Dict[str, str | int | float]]:
		"""
		Получение полной информации о дисках

		:return: словарь со всеми данными
		:rtype: Dict[str, Dict[str, str | int | float]]
		"""
		result = {}

		for disk_info in self.disks:
			disk = Disk(disk_info.get_name())
			disk_temp = '0 C'

			try:
				disk_temp = disk.get_temperature()
			except FileNotFoundError:
				disk_temp = 'N/A'

			result[f'{disk.get_name()}'] = {
				'path': disk.get_path(),
				'wwn': disk.get_wwn(),
				'model': disk.get_model(),
				'serial': disk.get_serial_number(),
				'firmware': disk.get_firmware(),
				'disk_type': disk.get_type(),
				'size': disk.get_size(),
				'device_id': disk.get_device_id(),
				'temperature': disk_temp,
				'physical_block_size': disk.get_physical_block_size(),
				'logical_block_size': disk.get_logical_block_size(),
				'partition_table_type': disk.get_partition_table_type(),
				'partition_table_uuid': disk.get_partition_table_uuid()
			}

		return result

	def get_partition_by_id(self, partition_id: int) -> Dict | None:
		"""
		Метод получения раздела по его id

		:return: информация о разделе или None
		:rtype: Dict | None
		"""
		try:
			return self.partitions[partition_id]
		except IndexError:
			return None

	def get_total_size_from_all_partitions(self) -> str:
		"""
		Получение общего размера всех разделов

		:return: человекочитаемый размер
		"""
		total_size = 0

		for partition in self.partitions:
			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue

			total_size += partition_usage.total

		return convert_to_human_size(total_size)

	def get_used_size_from_all_partitions(self):
		"""
		Получение размера использования всех разделов

		:return: человекочитаемый размер
		"""
		total_size = 0

		for partition in self.partitions:
			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue

			total_size += partition_usage.used

		return convert_to_human_size(total_size)

	def get_free_size_from_all_partitions(self):
		"""
		Получение свободного размера всех разделов

		:return: человекочитаемый размер
		"""
		total_size = 0

		for partition in self.partitions:
			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue

			total_size += partition_usage.free

		return convert_to_human_size(total_size)

	def get_io_statistics(self) -> Dict[str, str]:
		"""
		Получение статистики ввода/вывода

		:return: словарь с информацией
		:rtype: Dict[str, str]
		"""
		disk_io = psutil.disk_io_counters()

		return {
			'read': convert_to_human_size(disk_io.read_bytes),
			'write': convert_to_human_size(disk_io.write_bytes)
		}

	def get_partitions_info(self) -> Dict[str, str]:
		"""
		Получение информации обо всех разделов

		:return: словарь с информацией
		:rtype: Dict[str, str]
		"""
		partitions_info = {}

		for partition in self.partitions:
			device_name = str(partition.device)
			partitions_info[device_name] = {}
			partitions_info[device_name]['mountpoint'] = str(partition.mountpoint)
			partitions_info[device_name]['fstype'] = str(partition.fstype)

			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue

			partitions_info[device_name]['total'] = convert_to_human_size(partition_usage.total)
			partitions_info[device_name]['used'] = convert_to_human_size(partition_usage.used)
			partitions_info[device_name]['free'] = convert_to_human_size(partition_usage.free)
			partitions_info[device_name]['percent'] = f'{partition_usage.percent}%'

		return partitions_info

	def get_full_info(self) -> Dict[str, str]:
		"""
		Получение информации о диске, разделах и статистике

		:return: словарь с информацией
		:rtype: Dict[str, str]
		"""
		result = {
			'total_size_from_all_partitions': self.get_total_size_from_all_partitions(),
			'used_size_from_all_partitions': self.get_used_size_from_all_partitions(),
			'free_size_from_all_partitions': self.get_free_size_from_all_partitions(),
			'partitions_info': self.get_partitions_info(),
			'statistics': self.get_io_statistics(),
			'full_info': self.get_full_disk_info()
		}

		return result
