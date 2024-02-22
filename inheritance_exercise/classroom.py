class Person:
        def __init__(self, firstname, lastname):
                self.firstname = firstname
                self.lastname = lastname
        def __str__(self):
                return("%s %s" % (self.firstname, self.lastname))

class Student(Person):
        def __init__(self, firstname, lastname, subject):
                Person.__init__(self, firstname, lastname)
                self.subject = subject
        def __str__(self):
                return("%s %s, %s" % (self.firstname, self.lastname, self.subject))

class Teacher(Person):
	def __init__(self, firstname, lastname, course):
		Person.__init__(self, firstname, lastname)
		self.course = course
	def __str__(self):
		return("%s %s, %s" % (self.firstname, self.lastname, self.course))

