list=[10,20,30,40,50];
print("list before reverse",list);
L=0
R=(len (list)-1)

while L<R:
	temp=list[L]
	list[L]=list[R]
	list[R]=temp
	L=L+1
	R=R-1
	
print("list after reverse",list);