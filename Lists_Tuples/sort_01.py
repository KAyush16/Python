even=[2,4,6,8]
odd=[1,3,5,7,9]

even.extend(odd)
print(even)
even.sort(reverse=False)# return in ascending order same like even.sort()
print(even)
even.sort(reverse=True) # return in decending order 
print(even)