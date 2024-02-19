list1 = [1,2,3,4,5]

print(len(list1))

number_lis = list(range(1,4))
print(number_lis)

colours = ["purple","teal","yellow"]
print(colours[1])

''' Accessing the valus in a list using loops'''
numbers = [1,2,3,5,7,10]

for num in numbers:
    print(num)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
'''concatenation of the values in a loop'''
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""

for index in sounds:
	index1 = index.upper() #converts to upper
	result = result+index1

print(result)


# list comprehension
original = "this is so much fun"
new = ''.join(x for x in original if x not in 'aeiou')
print(new)