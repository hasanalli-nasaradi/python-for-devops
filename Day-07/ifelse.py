import sys

type = sys.argv[1]

if type == "t2.micro":
    print("we will create you a t2.micro instance")
elif type == "t2.small":
    print("we will create you a t2.small instance")
elif type == "t2.medium":
    print("we will create you a t2.medium instance")
else:
    print("please provide valid instance type")