
import sys
import shlex
import subprocess
import os

class Console:

	def message(self, message):
		sys.stdout.write(message.strip() + "\n")

	def success(self, message):
		self.message('--> ' + message)

	def error(self, message):
		self.message('error: ' + message)

	def run(self, args, cwd=None):
		self.message('$ ' + ' '.join(args))
		proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
		stdout, stderr = proc.communicate()
		if len(stderr):
			self.error(stderr)
		return stdout
