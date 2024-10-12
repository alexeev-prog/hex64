import sys
import json
from threading import Thread
from time import sleep
from PyQt5 import QtWidgets
from hex64_diagnostic.infrastructure.sensors.cpu import CPUSensor
from hex64_diagnostic.infrastructure.sensors.ram import RAMSensor
from hex64_diagnostic.infrastructure.sensors.temp import TempSensor
from hex64_diagnostic.infrastructure.sensors.disk import DiskSensor
from hex64_diagnostic.infrastructure.sensors.network import NetworkSensor
from hex64_diagnostic.infrastructure.repositories.hardware_repository import HardwareDataManager
from hex64_diagnostic.infrastructure.data.processor_info import ProcessorInfoData
from hex64_diagnostic.plots.plots_generator import CPUPlotGenerator, RAMPlotGenerator, DiskPlotGenerator, TempPlotGenerator, NetworkPlotGenerator
from hex64_diagnostic.utils.other import get_current_datetime
import hex64_diagnostic.interfaces.gui.application_ui as ui_design


class hex64App(QtWidgets.QMainWindow, ui_design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.label_4.setText("""
---------------------------------------------------------------------------------
   __ _______  __  ____ ____         hex64 Diagnostic v0.12.17
  / // / __/ |/_/ / __// / /         PC Monitoring, Analysing, Diagnostic Toolkit
 / _  / _/_>  <  / _ /_  _/         developed by alxvdev
/_//_/___/_/|_|  ___/ /_/           https://github.com/alxvdev/hex64
---------------------------------------------------------------------------------
			""")

		self.cpu_sensor = CPUSensor()
		self.temp_sensor = TempSensor()
		self.ram_sensor = RAMSensor()
		self.disk_sensor = DiskSensor()
		self.network_sensor = NetworkSensor()

		self.hdm = HardwareDataManager(self.cpu_sensor, self.ram_sensor, self.temp_sensor, self.disk_sensor, self.network_sensor)
		self.pid = ProcessorInfoData()

		self.cpu_plot = CPUPlotGenerator(self.hdm)
		self.ram_plot = RAMPlotGenerator(self.hdm)
		self.disk_plot = DiskPlotGenerator(self.hdm)
		self.temp_plot = TempPlotGenerator(self.hdm)
		self.network_plot = NetworkPlotGenerator(self.hdm)

		self.update_labels_with_data()

		self.pushButton_6.clicked.connect(self.get_processor_description)

		self.pushButton_5.clicked.connect(lambda: Thread(target=self.cpu_plot.draw_bar_cpu_statistics).start())
		self.pushButton.clicked.connect(lambda: Thread(target=self.cpu_plot.draw_bar_cpu_frequency).start())
		self.pushButton_2.clicked.connect(lambda: Thread(target=self.cpu_plot.draw_bar_cpu_load_average).start())
		self.pushButton_3.clicked.connect(lambda: Thread(target=self.cpu_plot.draw_bar_cpu_times_percent).start())
		self.pushButton_7.clicked.connect(lambda: Thread(target=self.ram_plot.draw_bar_svmem_size).start())
		self.pushButton_8.clicked.connect(lambda: Thread(target=self.ram_plot.draw_bar_swap_size).start())

		self.pushButton_9.clicked.connect(lambda: Thread(target=self.save_disk_report).start())
		self.pushButton_10.clicked.connect(lambda: Thread(target=self.disk_plot.draw_bar_disks_sizes).start())
		self.pushButton_12.clicked.connect(lambda: Thread(target=self.disk_plot.draw_bar_disks_physical_block_size).start())
		self.pushButton_11.clicked.connect(lambda: Thread(target=self.disk_plot.draw_bar_disks_logical_block_size).start())

		self.pushButton_13.clicked.connect(lambda: Thread(target=self.save_temp_report).start())
		self.pushButton_14.clicked.connect(lambda: Thread(target=self.temp_plot.draw_bar_full_temps).start())

		self.pushButton_16.clicked.connect(lambda: Thread(target=self.save_network_report).start())
		self.pushButton_15.clicked.connect(lambda: Thread(target=self.network_plot.draw_bar_temp_by_sensor_name).start())

	def save_disk_report(self):
		with open(f'disk_{get_current_datetime(True)}.json', 'w') as file:
			json.dump(self.hdm.get_disk_info(), file, indent=4)

	def save_temp_report(self):
		with open(f'temp_{get_current_datetime(True)}.json', 'w') as file:
			json.dump(self.hdm.get_temp_info(), file, indent=4)

	def save_cpu_report(self):
		with open(f'temp_{get_current_datetime(True)}.json', 'w') as file:
			json.dump(self.hdm.get_cpu_info(), file, indent=4)

	def save_ram_report(self):
		with open(f'temp_{get_current_datetime(True)}.json', 'w') as file:
			json.dump(self.hdm.get_ram_info(), file, indent=4)

	def save_network_report(self):
		with open(f'temp_{get_current_datetime(True)}.json', 'w') as file:
			json.dump(self.hdm.get_network_info(), file, indent=4)

	def __update_cpu_thread(self):
		while True:
			self.hdm.update_data()

			self.label_6.setText(f'{self.hdm.get_cpu_info()["brand_raw"]} {self.hdm.get_cpu_info()["vendor_id_raw"]} {self.hdm.get_cpu_info()["bits"]}bits')
			self.label_7.setText(f"Количество физических ядер: {self.hdm.get_cpu_info()['physical_cores_count']}")
			self.label_10.setText(f"Всего ядер: {self.hdm.get_cpu_info()['total_cores_count']}")
			self.label_12.setText(f"Максимальная {self.hdm.get_cpu_info()['cpu_frequency']['max']}МГц, минимальная {self.hdm.get_cpu_info()['cpu_frequency']['min']}МГц, текущая {self.hdm.get_cpu_info()['cpu_frequency']['current']}МГц")
			self.label_9.setText(f'Процент использования: {self.hdm.get_cpu_info()["cpu_usage_percentage"]}%')
			self.label_11.setText(f'Статистика: {" ".join([f"{name}={value}" for name, value in self.hdm.get_cpu_info()["cpu_statistics"].items()])}')
			self.label_8.setText(f'Кэш процессора: l1 (data={self.hdm.get_cpu_info()["l1_data_cache_size"]}, instruction={self.hdm.get_cpu_info()["l1_instruction_cache_size"]})\nl2 (cache={self.hdm.get_cpu_info()["l2_cache_size"]}, line={self.hdm.get_cpu_info()["l2_cache_line_size"]}, associativity={self.hdm.get_cpu_info()["l2_cache_associativity"]})\nl3 (cache={self.hdm.get_cpu_info()["l3_cache_size"]})')

			ram_info = self.hdm.get_ram_info()

			self.label_13.setText(f"Всего виртуальной памяти: {ram_info['svmem_total_size']} ({ram_info['svmem_percentage']})")
			self.label_15.setText(f"Использовано виртуальной памяти: {ram_info['svmem_used_size']} / свободно виртуальной памяти: {ram_info['svmem_available_size']}")
			self.label_14.setText(f"Кэшировано виртуальной памяти: {ram_info['svmem_cached_size']}")
			self.label_16.setText(f"Shared виртуальной памяти: {ram_info['svmem_shared_size']}")
			self.label_17.setText(f"Всего памяти подкачки: {ram_info['swap_total_size']} ({ram_info['swap_percentage']})")
			self.label_18.setText(f"Использовано памяти подкачки: {ram_info['swap_used_size']}")
			self.label_19.setText(f"SIN памяти подкачки: {ram_info['swap_sin_size']}")
			self.label_20.setText(f"SOUT памяти подкачки: {ram_info['swap_sout_size']}")

			disk_info = self.hdm.get_disk_info()

			self.label_21.setText(f"Размер всех разделов всех дисков: {disk_info['total_size_from_all_partitions']}")
			self.label_22.setText(f"Использованный размер всех разделов: {disk_info['used_size_from_all_partitions']}")
			self.label_23.setText(f"Свободный размер всех разделах: {disk_info['free_size_from_all_partitions']}")
			self.label_25.setText(f"Статистика: записано {disk_info['statistics']['write']}, прочитано {disk_info['statistics']['read']}")
			self.label_24.setText(f"Пути до дисков: {' '.join(self.disk_sensor.get_disks_paths())}")

			temp_info = self.hdm.get_temp_info()

			self.label_26.setText(f"Температура процессора: {temp_info['cpu_temp']} C")
			self.label_27.setText(f"Текущая температура сенсоров: {temp_info['temps']}")

			result = ''

			for temp_list in self.temp_sensor.get_temperature_sensors_with_names():
				result += f'Сенсор {temp_list[0]}: текущая {temp_list[1]} C, максимальная {temp_list[2]} C, критическая {temp_list[3]} C\n'

			self.label_28.setText(result)

			net_info = self.hdm.get_network_info()

			net_statistics = ''

			for name, value in self.network_sensor.get_full_io_statistics().items():
				net_statistics += f'{name}: {value}\n'

			io_base_data = self.network_sensor.get_io_statistics()

			self.label_29.setText(f"I/O полная статистика: {net_statistics}")
			self.label_30.setText(f'Отправлено {io_base_data["sent"]} байтов, принято {io_base_data["recv"]} байтов')

			interfaces = self.network_sensor.get_all_addresses_info()

			interfaces_info = ''

			for interface in interfaces:
				interfaces_info += f'Имя интерфейса: {interface["interface_name"]} (IP {interface["ip_address"]}; netmask {interface["netmask"]}; broadcast IP {interface["broadcast_ip"]})\n'

			self.label_31.setText(f"Информация о сетевых интерфейсах:\n{interfaces_info}")

			sleep(1)

	def get_processor_description(self):
		brand_raw = self.hdm.get_cpu_info()['brand_raw'].replace(' Processor', '')
		info_dict = self.pid.get_processor_info(brand_raw)

		if len(info_dict) > 0:
			result = f'{brand_raw} - {info_dict["cpu_type"]}'

	def update_labels_with_data(self):
		thr = Thread(target=self.__update_cpu_thread)
		thr.start()


def launch_app():
	app = QtWidgets.QApplication(sys.argv)
	window = hex64App()
	window.show()
	app.exec_()
