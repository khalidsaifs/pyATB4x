'''List Operations: Given the list numbers = [1, 2, 3, 4, 5], perform the following operations:
Append 6 to the list.
Remove 3 from the list.
Sort the list in descending order.'''
my_list =[]
for i in range(1, 11):

    my_list.append(i)

print(my_list)
# my_list= [1, 2, 3, 4, 5]
my_list.append(16)
my_list.remove(3)
my_list.sort(reverse=True)
my_list.sort(reverse=False)
print(my_list)
