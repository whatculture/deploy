
import yaml

class Conf:

	def read(self, file):
		self.data = yaml.safe_load(open(file))

	def has(self, option):
		return self.data.has_key(option)

	def get(self, option, default=False):
		if self.has(option):
			return self.data[option]
		return default
