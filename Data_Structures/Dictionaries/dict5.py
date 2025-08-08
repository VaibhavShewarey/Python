d={1:'Geeks',2:'For',3:'Geeks','age':22}

del d["age"]
print(d)

val=d.pop(1)
print(val)

key,val=d.popitem()
print(f"Key: {key},Value:{val}")

d.clear()
print(d)

