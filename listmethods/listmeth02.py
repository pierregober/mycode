#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


#Challenge aka step 25
#example list
data = [45,45,22,334,545,2223,90,442,233]

#print before
print("BEFORE REMOVE METHOD: ", data)

#remove the first  entry === 45
data.remove(45)

#print after
print("AFTER REMOVE METHOD: ", data)
