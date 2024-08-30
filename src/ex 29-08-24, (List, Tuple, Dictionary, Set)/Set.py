#Set: Set is a collection of unique items.
#Set is denoted by {}
#in set duplicated are removd by itself and it doesnt have any order in output.
set1={"Apple","car","scooter"}
set2={"bag","egg","car"}
S=set1.union(set2)
d=set1.intersection(set2)
e=set2.difference(set1)
f=set1.issubset(set2)
print(S,d,e,f)


