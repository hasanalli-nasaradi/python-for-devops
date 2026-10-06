# import sys
# def add(num1 , num2):
#     add = num1 + num2
#     return add

# def sub(num1 , num2):
#     sub = num1 - num2
#     return sub

# def mul(num1 , num2):
#     mul = num1 * num2
#     return mul

# num1 = int(sys.argv[1])
# operation = sys.argv[2]
# num2 = int(sys.argv[3])

# if operation == "add":
#     result = add(num1, num2)
#     print(result)
# elif operation == "sub":
#     result = sub(num1,num2)
#     print(result)
# elif operation == "mul":
#     result = mul(num1,num2)
#     print(result)

# add password usng below command in powershell
# $env:password = "hasanalli" 
# $env:apitoken = "iznaiznaia=zna"
# run the below command in powershell to run the script

import os

password=os.getenv("password")
print(password)
apitoken=os.getenv("apitoken")
print(apitoken)
