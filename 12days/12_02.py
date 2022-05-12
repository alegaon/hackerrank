class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

import statistics
        
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        self.average = round(statistics.mean(scores))

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grade = ""
        if self.average >= 90 and self.average <= 100:
            grade = "O"
        elif self.average >= 90 and self.average <= 100:
            grade = "E"
        elif self.average >= 90 and self.average <= 100:
            grade = "A"
        elif self.average >= 90 and self.average <= 100:
            grade = "P"
        elif self.average >= 90 and self.average <= 100:
            grade = "D"
        else:
            grade = "T"
        # tengo a calcular el promedio
        # buscar como hago una funcio q acepta n cantidad de parametros desconocidos
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())