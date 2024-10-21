from typing import Dict


class ProcessorInfoData:
	def __init__(self):
		self.processors_info = {
			"AMD C-50": {
				"cpu_type": "ноутбучный",
				"total_cores_count": 2,
				"frequency": "1000 МГц",
				"turbo_boost": False,
				"family": "Ontario",
				"tech_process": "40нм",
				"ram_type": "DDR3 Single-channel",
				"socket": "FT1 BGA 413-Ball"
			}
		}

	def get_processor_info(self, name: str) -> Dict[str, str | int | bool]:
		try:
			return self.processors_info[name]
		except KeyError:
			return {}

	def add_new_data(self, name: str, data: dict) -> bool:
		if name not in self.processors_info:
			self.processors_info[name] = data
			return True
		else:
			return False
