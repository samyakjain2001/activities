i, j, _  = 7, 8, 9; 
print(type(i));
print(i, j)

a = '123'
print(int(a), type(int(a)));
a = '123.451'
b = float(a)
print(type(b))
print("123.451")
print("list: ", list(a))
print("set: ", set(a))
print("tuple: ", tuple(a))

e1 = (1, 23, 45) #tuple
print(e1)
# e1[0] = 6 #immutable
e1 = (6, 78, 90) #reassiganble
print(e1)
print()
ipl_captains = {
    "csk": "MS Dhoni",
    "mi": "Rohit Sharma",
    "srh": "K Williamson",
    "lsg": "KL Rahul"
}
ipl_captains["mi"] = "Ishan Kishan"
print(ipl_captains["mi"])
print(ipl_captains.keys())

print(pow(2,3))