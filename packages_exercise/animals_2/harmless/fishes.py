class Fishes:
        def __init__(self):
                ''' Constructor for this class. '''
                # Create some member animals
                self.members = ['Salmon', 'Tuna']

        def printMembers(self):
                print('Printing members of the harmless Fishes class')
                for member in self.members:
                        print('\t%s ' % member)

