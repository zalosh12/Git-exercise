from  collections import Counter
import json

class Address:
    def __init__(self,city,street):
        self.city = city
        self.street = street




class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def add_year(self):
        self.age += 1

u1 = User("Elazar",23)
json_data = json.dumps(u1.__dict__)
with open("file.json","w") as f:
    f.write(json_data)
data = json.loads(json_data)
print(data)

def object_to_dict(user):
    return {"user": user.name,"age":user.age}

def longest_word(string):
    return max(string.split(),key=len)

print(longest_word("jfryu kh l"))

def union(lst1,lst2):
    return list(set(lst1) & set(lst2))

def divisors(n):
    res = 0
    for i in range(1,int(n ** 0.5) + 1):
        if not n % i:
            res += i
    if (n ** 0.5).is_integer():
            res -= int(n ** 0.5)
    return res * 3
print(divisors(12))

def stars(n):
    if n == 1:
        print("*")
        return
    print("*" * n)
    stars(n - 1)
    print("*" * n)

stars(6)

def func(s):
    s = s.split()
    dic = {}
    for i in s
