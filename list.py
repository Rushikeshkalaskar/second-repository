list=list[10,20,30,40,50]
l=len(list)

i=0
print("forward direction fetching")
while i<l:
	print(list[i],end="\t")
	i=i+1
print("\nbackward direction fetching ")
j=-1
while j>=-l:
	print(list[j],end="\t")
	j=j-1
print()
print("End program");