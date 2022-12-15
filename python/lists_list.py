grocery = ["keyur", "patel"]
# print(grocery[1])

numbers = [1, 2, 4, 8, 9, 7, 6, 13]
# numbers.sort() # mutable
# numbers.reverse()
# numbers.append(5)
# numbers.insert(1, 67)
# numbers.remove(67)
# numbers.pop()
# print(numbers)

print(numbers[::-3])  # you can also use slice in array
# print(min(numbers))


# mutable -- can change
# immutable -- cannot change

tp = (1,)  # called tuples
# tp[1] = 9  # cannot change value in tuples... throws error...
# print(type(tp))


a = 1
b = 2
a, b = b, a  # swap  the value
# print(a, b)


list = [1, "keyur", 4, 9]

# for items in list:
#     # print(str(items))
#     if str(items).isnumeric() and items > 6:
#         print(items)

# for i in range(10):
#     print(i, end=" ")
