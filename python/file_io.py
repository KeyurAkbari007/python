# "r" - open file for reading -default mode
# "w" - open a file for write
# "x" - creates file if not exit
# "a" - add  more content to a file
# "t" - text mod  -default mode
# "b" - binary mod
# "+" - read and write

# t = open("keyur.txt", "rt")  # t is file pointer # rt read and text mode
# content = t.read()
# print(t.readline())
# print(t.readline())
# print(content)
# for line in t:  # print line by line
#     print(line)


# list
# print(t.readlines())

# t.close()


# t = open("keyur.txt", "w")
# a = t.write("hyyyy")
# print(a)  # return character of string # 5
# t.close()


# t = open("keyur.txt", "r+")
# print(t.read())
# t.write("keyur patel")
# print(t.read())
# t.close()


# keyur.txt

# hyyyykeyur patel
# hghhg
# hhhfhgh
# jh
# ghgh
# tht

# t = open("keyur.txt")
# # print(t.tell())  # 0
# print(t.readline())  # read one line
# # print(t.tell())  # 18
# print(t.readline())  # read next line
# # print(t.tell())  # 25
# print(t.readline())  # read  next line
# # print(t.tell())  # 34

# print(t.readlines())
# print(t.readline())  # print first line
# t.seek(0)  # file pointer reset to 0 character
# print(t.readline())  # print first line
# t.close()


# with open("a.txt") as f:
#     a = f.read(4)
#     print(a)
