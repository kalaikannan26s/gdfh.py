a11=int(input())
s=list(map(int,input().split()))
su11=0
se22=0
for i in range(a11):
	if i%2==0:
		su11=su11+s[i]
	else:
		se+=s[i]
print(max(su11,se22))
