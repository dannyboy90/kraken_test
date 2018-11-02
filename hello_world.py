# My hello world:
import re
pattern = re.compile("version (\d\.\d)")
with open('README.md', 'r') as myfile:
	for i, line in enumerate(myfile):
		for match in re.finditer(pattern, line):
			version= match.group()
	

print("Hello world! This master3!!! Version: " + str(version))
