student = {}
student["name"] = "Andrew"
student['age'] = '20'
student['major'] = 'Finance', 'MIS'
student['hobbies']= 'volleyball/golf', 'working out', 'reading'
student['State']= 'Tennessee'

print('Student Information:')
for key, value in student.items():
    print(f"{key}: {value}")


student['age'] = int(student['age']) + 1

print(f'Updated student age: {student['age']}')