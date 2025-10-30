students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.split(",")
        student = {"name": name, "house": house}
        students.append(student)



def get_name(_):
    return _["name"]



for _ in sorted(students, key=get_name):
    print(_["name"])




