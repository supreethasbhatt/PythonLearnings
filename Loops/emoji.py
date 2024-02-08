# ''' Code to print emoji in ascending order'''

# num = 1

# while num <= 9:
#     #print(num)
#     print("\U0001f600" * num)
#     num += 1


for i in range(1,11):
    #print(i)
    smiley1 = "\U0001f600"
    count = 1
    while count < i:
        #print(f"{count}")
        smiley = "\U0001f600"
        smiley1 += smiley
        count = count + 1
    print(f"{smiley1}")