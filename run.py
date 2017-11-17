#!/usr/bin/env python

import os
import sys

from deploy import Deploy
from console import Console

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'Missing config file location'
		sys.exit(0)

	config_path = os.path.abspath(sys.argv[1])

	d = Deploy()
	d.config.read(config_path)

	try:
		# deploy branch
		if len(sys.argv) == 3:
			d.deploy(sys.argv[2])

		# deploy master
		else:
			d.deploy()

	except RuntimeError, e:
		c = Console()
		c.error(str(e))
