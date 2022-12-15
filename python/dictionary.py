# dictionary is nothing but key value pairs

d1 = {
    "keyur": "patel",
    "student": {"uni.": "darshan"}
}
# d1["gujarat"] = "rajkot"
# print(type(d1))
# print(d1["student"])
# print(d1)
# print(d1["student"]["uni."])
# del d1["keyur"]  # delete
# print(d1)

# d3 = d1.copy()  # return shadow of d1
# d3 = d1  # d3 is pointer to d1 .... if you change in d1 then affect in d3
# print(d3)
d1.update({"keyur": "akbari"})
print(d1)
print(d1.keys())
print(d1.items())
print(d1.values())
