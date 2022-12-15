import random
# snake
# water
# gun


def who_is_win(user_input, computerr, userr):
    if user_input == 1:
        user = "snake"
    elif user_input == 2:
        user = "water"
    else:
        user = "gun"

    if user_input == 1:
        if computer == "water":
            print("lost")
            computerr += 1
        elif computer == "gun":
            print("lost")
            computerr += 1
        else:
            print("tie")
    elif user_input == 2:
        if computer == "snake":
            print("win")
            userr += 1
        elif computer == "gun":
            print("win")
            userr += 1
        else:
            print("tie")
    else:
        if computer == "snake":
            print("win")
            userr += 1
        elif computer == "water":
            print("lost")
            computerr += 1
        else:
            print("tie")
    i = 0
    while i < 10:
        user_input = int(input("1 for sanke anf 2 for water and 3 for gun"))
        random_array = ["snake", "water", "gun"]
        computer = random.choice(random_array)
        if user_input in inputt:
            who_is_win(user_input, computerr, userr)
    print(computerr, userr, end="\n")


inputt = [1, 2, 3]
flag = True
computerr = 0
userr = 0
random_array = ["snake", "water", "gun"]
computer = random.choice(random_array)
print(computer)
user_input = int(input("1 for sanke anf 2 for water and 3 for gun"))
if user_input in inputt:
    who_is_win(user_input, computerr, userr)
else:
    print("invalid")
