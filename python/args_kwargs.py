# def funnction1(a,b,c,d,e):
#     print(a,b,c,d,e) this is not valid

def function(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


kw = {"a": "patel", "keyur": "akbari", "maulik": "bhatt"}
item = ["keyur", "maulik", "jenil", "yash", "deep"]
function(*item, **kw)


# normal argument , args , kwargs parameter rul
