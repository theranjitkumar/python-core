class App:

    def __init__(self):
        print('constructor called..')

    def sayHello(self):
        name = 'Ranjit'
        print('hello ' + name)

class Student (App):
    
    def __init__(self):
        students = [{'name':'ranjit', 'city':'patna'}, {'name':'ajit', 'city':'patna'}]
        print('student constructor called')
        for x in students:
            print(x['name'] +'-'+ x['city'])

    def helloStudent(self):
        print('hello from student')

a = App()
s = Student()
# s.students
# s.sayHello()

