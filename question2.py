#creating empty dictionary
dog = {}
print("",type(dog))

#Adding features to  the dictionary
dog = {"name":"Rocky", "color":"Brown", "breed":"Pitbull", "legs":"Medium", "age":"4years"}
print('', dog)

#creating a dictionary
student = {}
#Adding key details to dictionary
student = {"first_name":"Harshith", "last_name":"Vallem", "gender":"Male", "age":"23", "marital status":"Single", "skill":"Python", "country":"India", "city":"Hanamkonda", "address":"3-9-2 Reddy Colony "}
print('',student)

#finding the length of student dictionary
print("length of student dictionary is :", len(student))

#finding the value of skills and its datatype in list format
list = [student['skill'],type(student['skill'])]
print("skills and type of skill is :",list)

#modifying skills values
student['skill']="Python,SQL"
print("",student)

#getting the dictionary  keys as list
print(student.keys())

#getting the  dictionary  values as list
print(student.values())
