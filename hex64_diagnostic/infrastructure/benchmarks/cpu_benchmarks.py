#!/usr/bin/python3
"""
hex64 Diagnostic - инструмент для диагностики, мониторинга и анализа ресурсов ПК.

Модуль BENCHMARKS/CPU_BENCHMARKS - отвечает за бенчмарки и стресс-тесты для
процессора разными способами.

Файл: cpu.pu
Путь до файла: hex64_diagnostics/infrastructure/benchmarks/cpu_benchmarks.py
"""
import time
from random import randint
from multiprocessing import Process, Queue
from datetime import datetime
from hashlib import sha512, sha256, md5
import psutil
import numpy as np
import sympy as sp


def calculate_hash_512(num_limit):
	for i in range(num_limit):
		string = f'{randint(1000, 9999)}{randint(1000, 9999)}'
		sha512(string.encode()).hexdigest()


def calculate_hash_256(num_limit):
	for i in range(num_limit):
		string = f'{randint(1000, 9999)}{randint(1000, 9999)}'
		sha256(string.encode()).hexdigest()


def calculate_hash_md5(num_limit):
	for i in range(num_limit):
		string = f'{randint(1000, 9999)}{randint(1000, 9999)}'
		md5(string.encode()).hexdigest()


def mining_simulation(zero_count: int=1):
	while True:
		hash_data = sha256()
		string = f'{randint(1000, 9999)}{randint(1000, 9999)}'
		hash_data.update(str(datetime.now()).encode('utf-8'))
		hash_data.update(string.encode('utf-8'))

		if hash_data.hexdigest().startswith("0" * (zero_count // 2)):
			break


def insert_sort(arr: int) -> None:
	"""Insertion sort algorithm."""
	N = len(arr)
	for top in range(1, N):
		k = top
		while k > 0 and arr[k - 1] > arr[k]:
			arr[k], arr[k - 1] = arr[k-1], arr[k]
			k -= 1


def selection_sort(arr: list) -> None:
	"""Selection sort algorithm."""
	N = len(arr)
	for pos in range(0, N-1):
		for k in range(pos+1, N):
			if arr[k] < arr[pos]:
				arr[k], arr[pos] = arr[pos], arr[k]


def bubble_sort(arr: list) -> None:
	"""Bubble sort algorithm."""
	N = len(arr)
	for bypass in range(1, N):
		for k in range(0, N-bypass):
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]


def count_sort(arr: list) -> None:
	"""Counting sort algorithm."""
	max_value = max(arr) + 1
	count = [0] * max_value
	output = [0] * len(arr)

	for num in arr:
		count[num] += 1

	for i in range(1, max_value):
		count[i] += count[i - 1]

	for num in reversed(arr):
		output[count[num] - 1] = num
		count[num] -= 1

	for i in range(len(arr)):
		arr[i] = output[i]


def quick_sort(arr):
	"""Quick sorting algorithm."""
	if len(arr) <= 1:
		return
	barrier = arr[0]
	L = []
	M = []
	R = []
	for x in arr:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	quick_sort(L)
	quick_sort(R)
	k = 0
	for x in L + M + R:
		arr[k] = x
		k += 1


def merge(A: list[int], B: list[int]) -> list[int]:
	"""Helper function for merge sort."""
	C = [0] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C


def merge_sort(arr: list[int]) -> None:
	"""Merge sort algorithm."""
	if len(arr) <= 1:
		return

	middle = len(arr) // 2
	L = [arr[i] for i in range(middle)]
	R = [arr[i] for i in range(middle, len(arr))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L, R)

	for i in range(len(arr)):
		arr[i] = C[i]


def fibonacci_iterative(n):
	a, b = 0, 1

	for _ in range(n):
		a, b = b, a + b

	return a


def fibonacci_recursive(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def matrix_multiplication(size):
	A = np.random.rand(size, size)
	B = np.random.rand(size, size)
	C = np.dot(A, B)

	return C


def generate_primes(n):
	sieve = [True] * (n + 1)
	sieve[0] = sieve[1] = False

	for i in range(2, int(n**0.5) + 1):
		if sieve[i]:
			for j in range(i*i, n + 1, i):
				sieve[j] = False

	primes = [i for i, prime in enumerate(sieve) if prime]

	return primes


def differentiate(expr, var):
	return sp.diff(expr, var)


def integrate(expr, var):
	return sp.integrate(expr, var)


def generate_random_array(minnum, maxnum):
	arr = []

	for i in range(1000, 10000):
		arr.append(i)

	return arr


def pi_calculation(pi_calculation_num):
	for i in range(pi_calculation_num):
		for x in range(1, 1000):
			3.141592 * 2 ** x  # Multiplying the number Pi by 2 to the power of xx


def pi_calculation_2(pi_calculation_num):
	for i in range(pi_calculation_num):
		for x in range(1, 1000):
			float(x) / 3.141592  # Dividing x by Pi
		

def pi_calculation_3(pi_calculation_num):
	for i in range(pi_calculation_num):
		for x in range(1, 1000):
			float(3.141592) / x  # Dividing the number Pi by x"


def mega_calculate(num):
	result = []
	total_num = 0

	for i in range(num):
		result.append(i ** num)

	for r in result:
		total_num += randint(r, r * 10) // 2 * num

	return total_num ** num


class CPUBenchmarkMultiprocessor:
	def _stress_test(self, queue, duration_in_seconds: int, multuplier: int=1):
		x = sp.symbols('x')

		start_time = time.time()
		fib_index = 10 * multuplier
		prime_limit = 10000 * multuplier
		square_limit = 10000 * multuplier
		matrix_size = 100 * multuplier
		meganum = 1000 * multuplier
		pi_calculation_num = 1000 * multuplier

		total_points = 0

		hopes = 0

		while (time.time() - start_time) < duration_in_seconds:
			hopes += 1
			random_array = generate_random_array(100 * multuplier, 100000 * multuplier)
			total_points += 1

			merge_sort(random_array)
			total_points += 1

			count_sort(random_array)
			total_points += 1

			bubble_sort(random_array)
			total_points += 1

			selection_sort(random_array)
			total_points += 1

			insert_sort(random_array)
			total_points += 1

			pi_calculation(pi_calculation_num)
			total_points += 3

			fibonacci_iterative(fib_index)
			total_points += 1 + fib_index // 10

			fibonacci_recursive(fib_index)
			total_points += 1 + fib_index // 10

			matrix_multiplication(matrix_size)
			total_points += 3

			pi_calculation(pi_calculation_num)
			total_points += 3

			pi_calculation_2(pi_calculation_num)
			total_points += 3

			pi_calculation_3(pi_calculation_num)
			total_points += 3

			mining_simulation(1 * multuplier)
			total_points += 3

			calculate_hash_md5(100 * multuplier)
			total_points += 1

			calculate_hash_256(100 * multuplier)
			total_points += 2

			calculate_hash_512(100 * multuplier)
			total_points += 3

			generate_primes(prime_limit)
			total_points += 2

			differentiate(sp.sin(x), x)
			total_points += 1

			integrate(sp.sin(x), x)
			total_points += 1

			for i in range(randint(10, square_limit)):
				i ** i
			total_points += 3

			mega_calculate(meganum)
			total_points += 3

			fib_index += 1

			total_points += hopes

		queue.put({'points': total_points, 'multuplier': multuplier, 'hopes': hopes, 
			'all_points': total_points * multuplier, 'finished': True})

	def start_stress_test(self, duration_in_seconds, multuplier):
		num_processes = psutil.cpu_count(logical=True)
		results = []

		processes = []

		for _ in range(num_processes):
			queue = Queue()
			p = Process(target=self._stress_test, args=(queue, duration_in_seconds, multuplier))
			processes.append((p, queue))
			p.start()

		for p, queue in processes:
			while True:
				result = queue.get()
				if "finished" in result:
					results.append(result)
					break

			p.join()

		final_results = {
			'total_all_points': sum(result['all_points'] for result in results),
			'total_points': sum(result['points'] for result in results),
			'hopes': sum(result['hopes'] for result in results),
			'individual_results': results,
			'multuplier': multuplier,
			'duration': duration_in_seconds                                                                  
		}

		return final_results


class CPUBenchmarkSingleCore:		
	def start_stress_test(self, duration_in_seconds: int, multuplier: int=1) -> tuple:
		x = sp.symbols('x')

		fib_index = 10 * multuplier
		prime_limit = 10000 * multuplier
		square_limit = 10000 * multuplier
		matrix_size = 100 * multuplier
		meganum = 1000 * multuplier
		pi_calculation_num = 1000 * multuplier

		total_points = 0

		hopes = 0

		start_time = time.time()
		while (time.time() - start_time) < duration_in_seconds:
			hopes += 1
			random_array = generate_random_array(1000 * multuplier, 100000 * multuplier)
			total_points += 1

			merge_sort(random_array)
			total_points += 1

			count_sort(random_array)
			total_points += 1

			bubble_sort(random_array)
			total_points += 1

			selection_sort(random_array)
			total_points += 1

			insert_sort(random_array)
			total_points += 1

			pi_calculation(pi_calculation_num)
			total_points += 3

			pi_calculation_2(pi_calculation_num)
			total_points += 3

			pi_calculation_3(pi_calculation_num)
			total_points += 3

			mining_simulation(1 * multuplier)
			total_points += 3

			calculate_hash_md5(100 * multuplier)
			total_points += 1

			calculate_hash_256(100 * multuplier)
			total_points += 2

			calculate_hash_512(100 * multuplier)
			total_points += 3

			fibonacci_iterative(fib_index)
			total_points += 1 + fib_index // 10

			fibonacci_recursive(fib_index)
			total_points += 1 + fib_index // 10

			matrix_multiplication(matrix_size)
			total_points += 3

			generate_primes(prime_limit)
			total_points += 2

			differentiate(sp.sin(x), x)
			total_points += 1

			integrate(sp.sin(x), x)
			total_points += 1

			for i in range(randint(10, square_limit)):
				i ** i

			total_points += 3

			mega_calculate(meganum)
			total_points += 3

			fib_index += 1

			total_points += hopes

		return {
			'points': total_points, 'multuplier': multuplier, 'hopes': hopes, 
			'all_points': total_points * multuplier
		}
