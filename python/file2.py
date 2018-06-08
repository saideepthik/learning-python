f = open('myfile.txt',"r")
lines= f.readlines()
f.close()
print (lines)

f = open('myfile.txt', "r")
lines = list(f)
f.close()

f = open('myfile2.txt',"w")
f.writelines(lines)
f.close()

