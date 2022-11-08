student = ("Luis", 100, "Male")

print(student.count("Luis"))
print(student.index("Male"))

for x in student:
    print(x)

if "Luis" in student:
    print("Luis is here!")
