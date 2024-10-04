#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль UTILS/data_convertor - вспомогательная часть кода, нужна для конвертации различных
типов данных в другие типы данных

Файл: data_convertor.pu
Путь до файла: hex64_diagnostics/utils/data_convertor.py
"""


def convert_to_human_size(bytes_size: int, suffix: str="iB") -> str:
	"""
	Вспомогательная функция конвертации байтов в человекочитаемый формат.

	:param bytes_size: размер байтов
	:type bytes_size: int
	:param suffix: суффикс наименования размера
	:type suffix: str
	
	:rtype: str
	:return: читаемый размер
	"""
	factor: int = 1024 												# Фактор деления

	for unit in ['', 'K', 'M', 'G', 'T', 'P']:
		if bytes_size < factor:
			return f"{bytes_size:.2f}{unit}{suffix}"
			
		bytes_size /= factor
