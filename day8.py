f = open("doc.txt","r+")
print(f.read())


f.close()
file= open("doc.txt", "r")
list=list(file.readlines())
print(list)