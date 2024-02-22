def max_magnitude(nums):
    return(max(abs(x) for x in nums))
    
print(max_magnitude([300,-1,1000]))

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values
def sum_even_values(*args):
    print(type(args))
    print(args)
    summ=0
    for i in args:
        if i%2 == 0 :
            summ = summ+i
    print(summ)
            
sum_even_values(1,3,5) # 12

#zip
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))