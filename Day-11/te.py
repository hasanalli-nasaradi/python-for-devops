my_dict ={"name":"ali","roll": 13,"address":"pune"}
my_dict["building"]= "symphony"
my_dict["roll"]= 15

if 'age' in my_dict:
    print("age is present")
else:
    print("age is not present")
for key, value in my_dict.items():
    print(key, value)