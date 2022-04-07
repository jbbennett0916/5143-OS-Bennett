class PP:
	def __init__(self):
		self.test = 15
		self.cp = self.test

pp = PP()

pp.test = 0

print(pp.test)
print(pp.cp)


algo = 'pb'

if algo == 'cc':
	print('cc')
elif algo == 'pb':
	pass
else:
	print('YOOOOOO')