import os
import shutil

print "Simple python script for cleaning my projects folder from trash"
print "*" * 20

for root, dirs, files in os.walk("/Users/g0rdan/Projects"):
	if os.path.isdir(root):
		if "/bin" in root or "/obj" in root:
			shutil.rmtree(root)