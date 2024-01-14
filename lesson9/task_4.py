import re
with open('text2.txt') as e, open('words.txt') as d:
	text, exceptions = e.read(), d.read().split()
for i in exceptions:
	text = re.sub(i, '*' * len(i), text, flags=re.I)
print(text)