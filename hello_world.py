# My hello world:
import re
pattern = re.compile("version (\d\.\d)")
with open('README.md', 'r') as myfile:
	for i, line in enumerate(myfile):
		for match in re.finditer(pattern, line):
			version= match.group()
	

print("Hello world! This is branch! Version: " + str(version))
