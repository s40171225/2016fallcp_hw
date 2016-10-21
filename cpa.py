content = open("cpa.txt").read()
print(content)
#這是單行註解
print()

result = content.splitlines()
#result 變數資料型別為list
print(result)
print()
#針對list資料，可以利用for迴圈列出其數列成員
num=1
for g in result:
	g_list=g.split(",")
	g_list=g_list[:-1]
	for m in g_list:
		print("group:",num,"member:",m)
	num=num+1

'''
for line in content.splitlines():
result.append(list(line.split(",")))
'''
