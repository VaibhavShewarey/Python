a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]
        
ans = []
for key in range(len(query)):
    print(key)
    val = dict.get(query[key],"None")
    ans.append(val)


print(*ans, sep='\n')