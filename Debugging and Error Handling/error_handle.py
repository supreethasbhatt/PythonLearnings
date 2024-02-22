# d = {"name":"mysore"}
# d["city"]

# def get(d,key):
#     try:
#         d[key]
#     except KeyError:
#         return None

# print(get(d,"city"))



try:
    number = int(input("Enter a number"))
except:
    print("It is not a number")
else:
    print(f"Entered number is {number}")
finally:
    print("Runs no matter what")