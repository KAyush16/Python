# creating test_number.txt file using "w" mode
with open("test_number.txt","w")as test:
    for i in range(11):
        print(i,file=test) 
        '''to print each number in new line'''
        #test.write(str(i)) 
'''to put the whole number 0-10 in a single line using write method, also within the write 
method it should be string not integer , that's why we used str(i) '''