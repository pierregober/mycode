#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

#display list1[1] whcih should only displau arista_eos
print(list1[1])

list2 = ["juniper"]

list1.extend(list2)

print(list1)

list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
# use the append operation to append list1 by list3
list1.append(list3)
# display the new complex list1
print(list1)

#display the list of IP addresses 
print(list1[4])


#display the 1st item in the list - 1st IP addy
print(list1[4][0])
