from pdb import line_prefix


fhandle = open('dummy.txt')
print(fhandle.read())
fhandle.seek(0)     #to keep the cursor at our desired index
print(fhandle.read())
fhandle.seek(3)
print(fhandle.read())
print(fhandle.readline()) #read line 1st line for 2nd print two tumes
print(fhandle.readlines()) #returns the content in list reads all the lines
fhandle.close() #to close 

with  open('dummy.txt') as my_file:
    print(my_file.readlines())

with  open('dummy.txt',"r+") as my_file2:
    my_file2.seek(12)
    text = (my_file2.write("Hey its new written line"))
    print(text)
#write mode create new file or overwrites existing one
with  open('dummy3.txt',"w") as my_file3:
    my_file3.seek(12)
    text = (my_file3.write("!!!!!!!!!!!Hey its new written line"))
    print(text)
#file paths
# with  open('#can give path/dummy3.txt',"w") as my_file5:
#     my_file5.seek(12)
#     text = (my_file3.write("!!!!!!!!!!!Hey its new written line"))
#     print(text)

