
import os
import sys

from deploy import Deploy

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'Missing config file location'
		sys.exit(0)

	config_path = os.path.abspath(sys.argv[1])

	d = Deploy()
	d.config.read(config_path)
	d.deploy();
