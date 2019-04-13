from Person import Person
from Student import Student
from Staff import Staff
import os

PersonObj = Person('', '',)
StudentObj = Student('', '', '', '', '')
StaffObj = Staff('', '', '', '')

os.system('cls')
print('Objectos iniciales')
print(PersonObj.toString())
print(StudentObj.toString())
print(StaffObj.toString())

PersonObj.setName('Obama')
PersonObj.setAddress('Calle 53')

print()
print('Persona editada')
print(PersonObj.toString())

StudentObj.setName('Obama')
StudentObj.setAddress('Calle 53')
StudentObj.setYear('12/12/12')
StudentObj.setProgram('SOFT ING')
StudentObj.setFee(2.2)

print()
print('Estudiante Editido')
print(StudentObj.toString())

StaffObj.setName('Obama')
StaffObj.setAddress('Calle 53')
StaffObj.setPay(3000)
StaffObj.setSchool('HIGH MUSICAL')

print()
print('Staff Editido')
print(StaffObj.toString())