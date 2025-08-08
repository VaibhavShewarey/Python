f=open("ocean.txt","r")

print("Filename: ",f.name)

print("Module: ",f.mode)

print("IS Closed?",f.closed)

f.close()
print("Is closed?",f.closed)