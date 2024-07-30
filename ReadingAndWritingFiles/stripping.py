def removeprifix(string: str , prefix : str)-> str:
    if string.startswith(prefix):
        return string[len(prefix):] 
# slicing from the length of the prefix to the end of the string
    else:
        return string[:]
    
def removesuffix(string : str , suffix : str)-> str:
    if suffix and string.endswith(suffix): #suffix=' ' should not call string[:-0]
        return string[ :-len(suffix)] 
# which slices the string up to the length of the string minus the length of the suffix, effectively removing the suffix. 
    else:
        return string[:]
         
         
filename='Jabberwocky.txt'

with open(filename) as poem:
    first = poem.readline().rstrip() # readline() is used to read a single line from the file
                                    # .rstrip() is used to remove the whitespaces from the right/last

print(first)

chars="' Twasebv "
# no_apostrophe = first.strip(chars) # strip() used to remove whitespaces or anything specified under the braces 
# print(no_apostrophe)
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
print('*'*80)
'''
for charcter in first[::-1]:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
'''

twas_removed=removeprifix(first,"'Twas")
print(twas_removed)

print()

toves_removed=removesuffix(first,"toves")
print(toves_removed)