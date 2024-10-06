#Tuple:It is a collection of data.
#Tuple is denoted by ().
#It is fixed data
#It consumes less momory.
#It is immutable.

my_tuple= ("Apple","car","scooter")


#my_list.append("Hulk") {Append doesnt works in tuple.}
#my_list.remove("Apple"){'tuple' object has no attribute 'remove'}
#my_list[2]="weed"{'tuple' object does not support item assignment}

#IF we want to append, remove or assignt the item we need to concert the tuple into list. As shown below.
my_List = list(my_tuple)
my_list =my_List

my_list.append("Hulk")
my_list.remove("Apple")
my_list[2]="weed"
print(my_list)
print(len(my_list))