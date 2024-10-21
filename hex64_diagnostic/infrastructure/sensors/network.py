#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль SENSORS/NETWORK - отвечает за получение данных о сетевом подключении. Является частью
инфраструктуры программы.

Файл: network.pu
Путь до файла: hex64_diagnostics/infrastructure/sensors/network.py
"""
from typing import Dict, List
import psutil
from hex64_diagnostic.utils.data_convertor import convert_to_human_size
from hex64_diagnostic.utils.other import get_current_datetime


class NetworkSensor:
	"""
	Сенсор информации о сети
	"""
	def __init__(self):
		"""
		Инициализация
		"""
		self.if_addrs = psutil.net_if_addrs()

	def update_data(self):
		self.if_addrs = psutil.net_if_addrs()

	def get_io_statistics(self) -> Dict[str, str]:
		"""
		Статистика полученных и отправленных байтов

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		net_io = psutil.net_io_counters()

		return {
			'sent': convert_to_human_size(net_io.bytes_sent),
			'recv': convert_to_human_size(net_io.bytes_recv)
		}

	def get_pernic_io_statistics(self) -> Dict[str, str]:
		"""
		Статистика полученных и отправленных байтов на каждый интерфейс

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		net_io = psutil.net_io_counters(pernic=True)

		result = {}

		for interface in net_io.items():
			result[interface] = {
				'sent': convert_to_human_size(interface.bytes_sent),
				'recv': convert_to_human_size(interface.bytes_recv)
			}

		return result

	def get_full_io_statistics(self) -> Dict[str, str]:
		"""
		Статистика полной io статистики

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		net_io = psutil.net_io_counters()

		return {
			'sent': net_io.bytes_sent,
			'recv': net_io.bytes_recv,
			'packets_sent': net_io.packets_sent,
			'packets_recv': net_io.packets_recv,
			'errin': net_io.errin,
			'errout': net_io.errout,
			'dropin': net_io.dropin,
			'dropout': net_io.dropout
		}

	def get_full_pernic_io_statistics(self) -> Dict[str, str]:
		"""
		Статистика полной статистики каждого интерфейса

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		net_io = psutil.net_io_counters(pernic=True)

		result = {}

		for interface_name, snetio in net_io.items():
			result[interface_name] = {
				'sent': convert_to_human_size(snetio.bytes_sent),
				'recv': convert_to_human_size(snetio.bytes_recv),
				'packets_sent': snetio.packets_sent,
				'packets_recv': snetio.packets_recv,
				'errin': snetio.errin,
				'errout': snetio.errout,
				'dropin': snetio.dropin,
				'dropout': snetio.dropout
			}

		return result

	def get_addresses_by_name(self, name: str) -> List[Dict[str, str]]:
		"""
		Метод получения адресов по имени интерфейс

		:param name: имя интерфейса
		:rtype: str

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		results = []
		interface_addresses = if_addrs[name]

		for address in interface_addresses:
			if str(address.family) == 'AddressFamily.AF_INET':
				results.append({'name': name, 'family': 'AF_INET', 'ip_address': address.address, 
								'netmask': address.netmask, 'broadcast_ip': address.broadcast})
			elif str(address.family) == 'AddressFamily.AF_PACKET':
				results.append({'name': name, 'family': 'AF_INET', 'mac_address': address.address, 
								'netmask': address.netmask, 'broadcast_mac': address.broadcast})

		return results

	def get_all_addresses_info(self):
		"""
		Метод получения информации о всех интерфейсах и адресах

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		results = []

		for interface_name, interface_addresses in self.if_addrs.items():
			for address in interface_addresses:
				results.append({'interface_name': interface_name, 'family': 'AF_INET', 'ip_address': address.address, 
							'netmask': address.netmask, 'broadcast_ip': address.broadcast})

		return results

	def get_net_connections(self, kind: str='all') -> Dict[str, str]:
		"""
		Статистика сетевых подключений

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		result = {}
		connections = psutil.net_connections(kind=kind)

		for connection in connections:
			result[f'{connection.fd}#{get_current_datetime()}'] = {
				'fd': connection.fd,
				'family': str(connection.family),
				'type': str(connection.type),
				'laddr': connection.laddr,
				'raddr': connection.raddr,
				'status': connection.status,
				'pid': connection.pid
			}

		return result

	def get_full_info(self) -> Dict[str, str]:
		"""
		Метод получения полной статистики

		:return: словарь со статистикой
		:rtype: Dict[str, str]
		"""
		return {
			'addresses_info': self.get_all_addresses_info(),
			'pernic_io': self.get_full_pernic_io_statistics(),
			'net_connections': self.get_net_connections()
		}
