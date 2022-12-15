def keyur():
    x = 20

    def keyur1():
        global x
        x = 80
    print(f"befor calling keyur1 {x}")
    keyur1()
    print(f"after calling  keyur {x}")


keyur()
print(x)
