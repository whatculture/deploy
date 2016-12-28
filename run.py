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
		# rollback
		if len(sys.argv) == 4 and sys.argv[2] == 'rollback':
			
			print "rolling back"
			print "------- ----"

			d.rollback(sys.argv[3])
		
		# deploy branch		
		if len(sys.argv) == 3:
			
			print "deploy branch"
			print "------ ------"
					
			d.deploy(sys.argv[2])

		# deploy master
		else:

			print "deply master branch"
			print "----- ------ ------"

			d.deploy()

	except RuntimeError, e:
		c = Console()
		c.error(str(e))
