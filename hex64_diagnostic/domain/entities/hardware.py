#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль ENTITIES/HARDWARE - отвечает за доменную бизнес-зону комплектующих.

Файл: hardware.py
Путь до файла: hex64_diagnostics/domain/entities/hardware.py
"""
from uuid import uuid4
from hex64_diagnostic.infrastructure.repositories.hardware_repository import HardwareDataManager


class HardwareComponent:
	def __init__(self, component_name: str, component_description: str, component_metrics: dict):
		self.component_name = component_name
		self.component_description = component_description
		self.component_metrics = component_metrics
		self.benchmark_id = self.get_new_benchmark_id()

	def get_new_benchmark_id(self):
		return f'{self.component_name}_{str(uuid4())[:8].upper()}'

	@property
	def component(self):
		return f'{self.component_name} ({self.component_description})'


class CPUComponent(HardwareComponent):
	def __init__(self, component_metrics: dict):
		super().__init__('CPU', 'Центральный процессор', component_metrics)


class RAMComponent(HardwareComponent):
	def __init__(self, component_metrics: dict):
		super().__init__('RAM', 'оперативная память', component_metrics)


class DiskComponent(HardwareComponent):
	def __init__(self, component_metrics: dict):
		super().__init__('Disk', 'Диск, установленный на компьютере (SSD, HDD)', component_metrics)


class DiskPartitionComponent(HardwareComponent):
	def __init__(self, component_metrics: dict):
		super().__init__('DiskPartition', 'Часть диска и его файловой системы', component_metrics)


class TempComponent(HardwareComponent):
	def __init__(self, component_metrics: dict):
		super().__init__('TempSensor', 'Сенсор температуры комплектующих', component_metrics)


def integrate_hardware_to_component_entity(hdm: HardwareDataManager):
	"""
	Функция интеграции сенсоров и железа в сущности компонентов
	"""
	pass
