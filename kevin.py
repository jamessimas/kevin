class Kevin(object):

	def __init__(self):
		self.name = 'Kevin'
		self.has_beard = True
		self.beard_length = 0
		self.has_axe = False
		self.has_honey = False
		self.nick_offerman = False

	def get_name(self):
		print('His name is %s.' % self.name)

	def get_beard_length(self):
		print('The length of %s\'s beard is %s inches.' % (self.name, self.beard_length))

		if self.beard_length > 5:
			print('Wow! What a beard!')

		if self.beard_length > 10:
			print('Wowza!!')

		if self.beard_length > 15:
			print('It is like a beautific vision!')

	def grow_beard(self):
		self.beard_length += 1

		print('Like wild grass on the serengeti, %s\'s beard grows. It is %s inches long.' % (self.name, self.beard_length))

		if self.beard_length > 14:
			self.nick_offerman = True
			print('POOF! %s transforms into Nick Offerman!' % self.name)
			self.name = 'Nick'

	def trim_beard(self):
		if self.beard_length > 0:
			self.beard_length -= 1
			print('Looking good!')
		
		else:
			print('Too little hair. You cannot go any shorter.')

	def shave_beard(self):
		self.beard_length = 0
		print('Blasphemy! You have ruined a work of art.')

	def gather_honey(self):
		self.has_honey = True
		print('You send %s out to gather honey. He is victorious!' % self.name)

	def get_axe(self):
		self.has_axe = True
		print('And my axe!')

	def chop_wood(self):
		if self.has_axe is False:
			print('%s has no axe! Get yoself an axe, fool.' % self.name)
		else:
			print('Chop! Chop! Chop!')
