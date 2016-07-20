
import sys
import subprocess
import os

class Console:

	def message(self, message):
		sys.stdout.write(message.strip() + "\n")

	def success(self, message):
		self.message('--> ' + message)

	def error(self, message):
		self.message('error: ' + message)

	def run(self, command, cwd=None):
		proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
		stdout, stderr = proc.communicate()
		return stdout
