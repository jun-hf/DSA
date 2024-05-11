import sys

name = sys.argv[1]

fileName = "binary_search{0}.py".format(name)

f = open(fileName, "w")
f.write("import math\nfrom typing import List\nimport binaryTest\n\ndef binary_search():\n\nbinaryTest.test(binary_search)")
f.close()