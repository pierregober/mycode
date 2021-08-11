#!/usr/bin/env python3
# standard, don't need to install!
import argparse

# this object will hold all arguments the user passes in
parser_mcgee = argparse.ArgumentParser(
    description="For IP address and vendor info")

# acceptable values
acc_ip = ["awesome", "stunning", "intelligent"]

# add some arguments!
parser_mcgee.add_argument("ip", choices=acc_ip, help="This is the ip for you.")

# add an optional argument
parser_mcgee.add_argument("-a", metavar="ADVERB", default="so",
                          help="'Helper' words, like 'really, very, extremely', etc.")


# ================ Original Code Below

user_input = input("Please enter an IPv4 IP address:")

# the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

# print() can be given a series of objects separated by a comma
# print("You told me the IPv4 address is:", user_input)

# Step 15
vendor_name = input("Please enter a vendor name:")
# print("You told me the vendor name is:", vendor_name)


# have the parser obj turn all those arguments into variables
arglebargle = parser_mcgee.parse_args()
print(f"You have is {arglebargle.a} {arglebargle.ip}!")
