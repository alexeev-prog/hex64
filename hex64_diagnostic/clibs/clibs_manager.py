# TODO: integrate binary components
from typing import List
import ctypes


class CLibrary:
	def __init__(self, filepath: str):
		self.filepath = filepath
		self.cdll = ctypes.CDLL(self.filepath)


class CLibManager:
	def __init__(self, clibraries: List[CLibrary] | Dict[str, CLibrary]):
		self.clibraries = clibraries

	def get_library_by_index(self, index: int):
		return self.clibraries[index]

         
ram_lib = CLibrary("hex64_diagnostic/clibs/bin/ram.so")

ram_lib.cdll.machine_info()
