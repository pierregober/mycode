#!/usr/bin/env python3
# create a list containing 3 items
my_list = ["192.168.0.5", 5060, "UP"]

#display the 1st item in the list
print("The first item in the list (IP): " + my_list[0])

#display the 2nd item in the list
print("The second item in th list (port): " + str( my_list[1]))

#display the 3rd item in the list
print("The last item in the list (state): " + my_list[2])

#challenge
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print(iplist[3], iplist[4])
