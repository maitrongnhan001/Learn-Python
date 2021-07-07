class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        '''Tell my details'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        super().tell();
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print('(Initialized Student: {}'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Nhan', 31, 30000)
s = Student('Mai Trong Nhan', 21, 4)

print()

members = [t, s]
for member in members:
    member.tell()