#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль REPOSITORIES/HARDWARE_REPOSITORY - отвечает за хранение и доступ к данным бенчмарков.
Является частью инфраструктуры программы.

Файл: benchmark_repository.pu
Путь до файла: hex64_diagnostics/infrastructure/repositories/benchmark_repository.py
"""
from uuid import uuid4
from hex64_diagnostic.utils.other import get_current_datetime
from hex64_diagnostic.infrastructure.benchmarks.cpu_benchmarks import CPUBenchmarkSingleCore, CPUBenchmarkMultiprocessor


class CPUBenchmarkDataManager:
	def __init__(self, single_benchmark: 'CPUBenchmarkSingleCore', multi_benchmark: 'CPUBenchmarkMultiprocessor'):
		self.single_benchmark = single_benchmark
		self.multi_benchmark = multi_benchmark
		self.current_benchmark_number = 0

		self.benchmark_data = {}

	@property
	def benchmark_id(self):
		return f'{self.current_benchmark_number}#{str(uuid4())[:8].upper()}'

	def start_benchmark(self, benchmark_type: str, duration_in_seconds, multuplier: int):
		self.current_benchmark_number += 1
		result = {}

		current_benchmark_id = self.benchmark_id

		print(f'CPU Benchmark {current_benchmark_id}: {benchmark_type}, duration {duration_in_seconds}s, multuplier {multuplier}.')

		if benchmark_type == 'single':
			result = self.single_benchmark.start_stress_test(duration_in_seconds, multuplier)
		elif benchmark_type == 'multi':
			result = self.multi_benchmark.start_stress_test(duration_in_seconds, multuplier)
		else:
			return {}

		self.benchmark_data[current_benchmark_id] = {
			'benchmark_number': self.current_benchmark_number,
			'benchmark_type': benchmark_type,
			'date': get_current_datetime(),
			'duration': duration_in_seconds,
			'multuplier': multuplier,
			'result': result,
			'benchmark_id': current_benchmark_id
		}

		return self.benchmark_data[current_benchmark_id]
