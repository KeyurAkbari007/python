mystr = "keyur patel is study in darshan university"

print(mystr[0:4])  # string slicing

print(len(mystr))

print(mystr[0:5:2])  # skip one char after print one char

print(mystr[-4:-2])  # start from including -2 to excluding -4


print(mystr.isalnum())  # false
print(mystr.endswith("sity"))  # true
print(mystr.count("u"))  # 3
print(mystr.capitalize())  # capitalize first letter
print(mystr.find("uni"))
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("uni", "Uni"))
