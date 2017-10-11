tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t%s
\t* Fishies
\t* Catnip\n\t* Grass
''' % "* Cat food"

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

x = 0
while x < 10:
	for i in ["/", "-", "|", "\\", "|"]:
		print(i)
		x = x + 1