'''
age=34
print("My age is {0} years".format(age))
print("""Jan:{2}
Feb:{0}
Mar:{2}
April:{1}
May:{2}
June:{1}
July:{2}
Aug:{2}
Sep:{1}
Oct:{2}
Nov:{1}
Dec:{2}
""".format(28,30,31))
for i in range(1,13):
    print("Number {0} squared is {1} and cubed is {2}".format(i,i**2,i**3))

for i in range(1,13):
    print("Number {0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))
    
# f string 

age=24
print(f"my age is {age} years")
print(f"The value of pi is{22/7:12.50f}")
'''

name=input("Enter your name: ")
age=int(input("What is your age {0}? ".format(name)))
print(age)