
import sys
import shlex
import subprocess
import os

class Console:

	def message(self, message):
		sys.stdout.write(message.strip() + "\n")

	def success(self, message):
		self.message('\e[32m--> \e[39m' + message)

	def error(self, message):
		self.message('\e[31merror: \e[39m' + message)

	def run(self, args, cwd=None):
		self.message('command --> ' + ' '.join(args))
		proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
		stdout, stderr = proc.communicate()
		return stderr
