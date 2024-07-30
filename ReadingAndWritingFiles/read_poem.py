'''
jabber=open('Jabberwocky.txt','r')

for line in jabber:
    #print(line,end="")
    print(line.strip())
jabber.close()
'''
with open('Jabberwocky.txt' , 'r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    #lines = jabber.readlines()
    lines=jabber.read() # this will print string 
    
print(lines)
print(lines[-1:])

'''
for line in reversed(lines):
    print(line, end='') # do some processing in reversed order 
    
'''
 
for charcters in reversed(lines):
    print(charcters, end='')