class Mammals:
	def __init__(self):
	        ''' Constructor for this class. '''
	        # Create some member animals
	        self.members = ['Tiger', 'Elephant', 'Wild Cat']
	def dangerous(self):
		self.members = ['Tiger', 'Elephant']
	def harmless(self):
		self.members = ['Wild Cat']
	def printMembers(self):
	        print('Printing members of the Mammals class')
	        for member in self.members:
		        print('\t%s ' % member)
