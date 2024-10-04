#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль PLOTS/PLOTS_GENERATOR - отвечает за построение и вывод графиков об информации с 
сенсоров. Является частью инфраструктуры программы.

Файл: plots_generator.pu
Путь до файла: hex64_diagnostics/plots/plots_generator.py
"""
import matplotlib.pyplot as plt
from hex64_diagnostic.infrastructure.repositories.hardware_repository import HardwareDataManager
from hex64_diagnostic.infrastructure.repositories.benchmark_repository import CPUBenchmarkDataManager


class GeneralSensorPlotting:
	def __init__(self, hdm: HardwareDataManager):
		self.hdm = hdm


class GeneralBenchmarkPlotting:
	def __init__(self, cpu_bdm: CPUBenchmarkDataManager):
		self.cpu_bdm = cpu_bdm

	def start_single_benchmark(self, duration_in_seconds, multuplier):
		data = self.cpu_bdm.start_benchmark('single', duration_in_seconds, multuplier)

		x = ['Общий результат', 'Очки', 'Множитель', 'Повторения', 'Длительность']
		y = [data['result']['all_points'], data['result']['points'], data['result']['multuplier'],
			data['result']['hopes'], data['duration']]

		plt.bar(x, y, label='Результаты бенчмарка')
		plt.xlabel('Типы данных')
		plt.ylabel('Данные')
		plt.title(f'Информация о CPU однопроцессорном бенчмарке {data["current_benchmark_id"]}')
		plt.legend()

		plt.show()

	def start_multi_benchmark(self, duration_in_seconds, multuplier):
		data = self.cpu_bdm.start_benchmark('multi', duration_in_seconds, multuplier)

		data_result = data['result']

		x = ['Общий результат', 'Очки', 'Множитель', 'Повторения', 'Длительность']
		y = [data_result['total_all_points'], data_result['total_points'], data_result['multuplier'],
			data_result['hopes'], data_result['duration']]

		plt.bar(x, y, label='Результаты бенчмарка')
		plt.xlabel('Типы данных')
		plt.ylabel('Данные')
		plt.title(f'Информация о CPU мультипроцессорном бенчмарке {data["current_benchmark_id"]}')
		plt.legend()

		plt.show()


class DiskPlotGenerator(GeneralSensorPlotting):
	def __init__(self, hdm: HardwareDataManager):
		super().__init__(hdm)

	def draw_bar_disks_sizes(self):
		disk_info = self.hdm.get_disk_info()['full_info']

		x = []
		y = []

		for disk_name, info in disk_info.items():
			x.append(disk_name)
			y.append(info['size'])

		plt.bar(x, y, label='Размер дисков')
		plt.xlabel('Диск')
		plt.ylabel('Размер в байтах')
		plt.title('Информация о размере всех дисков')
		plt.legend()

		plt.show()

	def draw_bar_disks_physical_block_size(self):
		disk_info = self.hdm.get_disk_info()['full_info']

		x = []
		y = []

		for disk_name, info in disk_info.items():
			x.append(disk_name)
			y.append(info['physical_block_size'])

		plt.bar(x, y, label='Размер дисков')
		plt.xlabel('Диск')
		plt.ylabel('Физический размер блока')
		plt.title('Информация о размере блоков')
		plt.legend()

		plt.show()

	def draw_bar_disks_logical_block_size(self):
		disk_info = self.hdm.get_disk_info()['full_info']

		x = []
		y = []

		for disk_name, info in disk_info.items():
			x.append(disk_name)
			y.append(info['logical_block_size'])

		plt.bar(x, y, label='Размер дисков')
		plt.xlabel('Диск')
		plt.ylabel('Логический размер блока')
		plt.title('Информация о размере блоков')
		plt.legend()

		plt.show()


class NetworkPlotGenerator(GeneralSensorPlotting):
	def __init__(self, hdm: HardwareDataManager):
		super().__init__(hdm)

	def draw_bar_io_statistics(self):
		info = self.hdm.network_data.get_full_io_statistics()

		x = [name for name, _ in info.items()]
		y = [value for _, value in info.items()]

		plt.bar(x, y, label='Полная IO статистика')
		plt.xlabel('Тип')
		plt.ylabel('Размер в байтах')
		plt.title(f'Информация о I/O сети')
		plt.legend()

		plt.show()


class TempPlotGenerator(GeneralSensorPlotting):
	def __init__(self, hdm: HardwareDataManager):
		super().__init__(hdm)

	def draw_bar_temp_by_sensor_name(self, sensor_name: str):
		info = self.hdm.temp_data.get_info_by_name(sensor_name)

		x = ['Текущее', 'Высокая', 'Критическая']
		y = [info['current'], info['high'], info['critical']]

		plt.bar(x, y, label='Температура')
		plt.xlabel('Тип')
		plt.ylabel('Температура в градусах Цельсия')
		plt.title(f'Информация о температурном сенсоре {sensor_name}')
		plt.legend()

		plt.show()

	def draw_bar_full_temps(self):
		info = self.hdm.temp_data.get_temperature_sensors_with_names()

		x = [i[0] for i in info]
		y = [i[1] for i in info]

		plt.bar(x, y, label='Температура')
		plt.xlabel('Сенсор')
		plt.ylabel('Температура в градусах Цельсия')
		plt.title('Информация о всех температурах устройства')
		plt.legend()

		plt.show()


class RAMPlotGenerator(GeneralSensorPlotting):
	def __init__(self, hdm: HardwareDataManager):
		super().__init__(hdm)

	def draw_bar_svmem_size(self):
		total_size = self.hdm.ram_data.get_svmem_total_size(True)
		available_size = self.hdm.ram_data.get_svmem_available_size(True)
		used_size = self.hdm.ram_data.get_svmem_used_size(True)
		cached_size = self.hdm.ram_data.get_svmem_cached_size(True)
		shared_size = self.hdm.ram_data.get_svmem_shared_size(True)

		x = ['Общее количество', 'Доступно', 'Занято', 'Кешировано', 'Shared']
		y = [total_size, available_size, used_size, cached_size, shared_size]

		plt.bar(x, y, label='Размер ОЗУ')
		plt.xlabel('Тип')
		plt.ylabel('Размер в байтах')
		plt.title('Диаграмма объема ОЗУ')
		plt.legend()

		plt.show()

	def draw_bar_swap_size(self):
		total_size = self.hdm.ram_data.get_swap_total_size(True)
		used_size = self.hdm.ram_data.get_swap_used_size(True)
		sin_size = self.hdm.ram_data.get_swap_sin_size(True)
		sout_size = self.hdm.ram_data.get_swap_sout_size(True)

		x = ['Общее количество', 'Занято', 'sin', 'sout']
		y = [total_size, used_size, sin_size, sout_size]

		plt.bar(x, y, label='Размер файла подкачки')
		plt.xlabel('Тип')
		plt.ylabel('Размер в байтах')
		plt.title('Диаграмма объема файла подкачки')
		plt.legend()

		plt.show()


class CPUPlotGenerator(GeneralSensorPlotting):
	def __init__(self, hdm: HardwareDataManager):
		super().__init__(hdm)

	def draw_bar_cpu_frequency(self):
		cpu_info = self.hdm.get_cpu_info()

		x = ['Максимальная частота процессора', 'Текущая частота процессора', 'Минимальная частота процессора']
		y = [cpu_info['cpu_frequency']['max'], cpu_info['cpu_frequency']['current'], cpu_info['cpu_frequency']['min']]

		plt.bar(x, y, label='Частота в ГГц')
		plt.xlabel('Тип')
		plt.ylabel('Частота')
		plt.title(f'Диаграмма частоты процессора {cpu_info["processor"]}')
		plt.legend()

		plt.show()

	def draw_bar_cpu_load_average(self):
		cpu_info = self.hdm.get_cpu_info()

		x = [i for i in range(len(cpu_info['cores_usage_percentage']))]
		y = [i for i in cpu_info['cores_usage_percentage']]

		plt.bar(x, y, label='Частота в ГГц')
		plt.xlabel('Тип')
		plt.ylabel('Частота')
		plt.title(f'Диаграмма средней загруженности {cpu_info["processor"]}')
		plt.legend()

		plt.show()

	def draw_pie_cpu_times_percent(self):
		cpu_info = self.hdm.get_cpu_info()

		labels = []
		vals = []

		for name, num in cpu_info['cpu_times_percent'].items():
			labels.append(name)
			vals.append(num)

		plt.pie(vals, labels=labels, autopct="%1.1f%%")
		plt.title(f'Диаграмма cpu_times_percent {cpu_info["processor"]}')

		plt.show()

	def draw_bar_cpu_times_percent(self):
		cpu_info = self.hdm.get_cpu_info()

		labels = []
		vals = []

		for name, num in cpu_info['cpu_times_percent'].items():
			labels.append(name)
			vals.append(num)

		plt.bar(labels, vals, label='Средняя загруженность')
		plt.xlabel('Тип')
		plt.ylabel('Процент')
		plt.title(f'Диаграмма средней загруженности {cpu_info["processor"]}')
		plt.legend()

		plt.show()

	def draw_bar_cpu_statistics(self):
		cpu_info = self.hdm.get_cpu_info()

		labels = []
		vals = []

		for name, num in cpu_info['cpu_statistics'].items():
			labels.append(name)
			vals.append(num)

		plt.bar(labels, vals, label='Статистика')
		plt.xlabel('Тип')
		plt.ylabel('Значение')
		plt.title(f'Диаграмма статистики процессора {cpu_info["processor"]}')
		plt.legend()

		plt.show()
