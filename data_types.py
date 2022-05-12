# This brief class will consider the different data types used in programming langauges
# These include:
#       1 integer
#       2 string
#       3 floating point/real
#       4 boolean
#       5 one dimensional arrays / multidimensional
#       6 records

# 1 - integer
# x = 1
# y = 100
# z = x + y
# print(float(z))

# 2 - string
# name = "Andrew"
# print("Welcome, "+name)

# 3 - float
# x = 1.1
# y = 111.453
# z = x + y
# print(x+y)

# 4 - boolean
# ninja = True
# print(type(ninja))

# 5 - arrays
# cpu_components = ["Program Counter", "ALU", "Accumulator", "Control Unit", "General Purpose Registers"]
# print(cpu_components[0])
# for i in cpu_components:
#     print(i)

# 5b - multidimensional arrays
# pc = [["Keyboard","Mouse","Monitor"],["GPU","CPU","RAM"],["Operating System","Utility Software","Application Software"]]
# print(pc[0])
# print(pc[0][0])

# 6 - records
# from pyrecord import Record
# Student = Record.create_type("Student", "name", "email_address", "subjects")
# terry_student = Student("Terry Tibs", "ttibs@gmail.com", ["SDD", "Maths", "English"])
# mark_student = Student("Mark Robinson", "MR@gmail.com", ["English", "Maths", "History"])
# print(terry_student.email_address)
# print(mark_student.email_address, mark_student.subjects[0])

# 7 - bonus - arrays of records (database)
# from pyrecord import Record
# Student = Record.create_type("Student", "name", "email_address", "subjects")
# mark_student = Student("Mark Albrighton", "markalbrighton@gmail.com", ["History", "Maths", "English"])
# terry_student = Student("Terry Tibs", "ttibs@gmail.com", ["SDD", "Maths", "English"])
# ian_student = Student("Iain Wood", "iwood@gmail.com", ["Economics", "RS", "English"])
# students = [mark_student, terry_student, ian_student]
# for i in students:
#     print(i)
