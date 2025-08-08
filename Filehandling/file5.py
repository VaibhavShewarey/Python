try:
    file=open("ocean.txt","r")
    content=file.read()
    print(content)
finally:
    file.close()