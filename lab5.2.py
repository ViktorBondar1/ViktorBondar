sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

 for key, value in sample_dict.items():
     print(f'{key:<10} : {value:>10}')

for key in sample_dict.keys():
print(key, sample_dict[key])

l1=["age", "salary", "name"]
fore key in l1:
 if key in sample_dict:
   newdict[key]= sample_dict[key]

print(newdict)

for i in l1:
    print(sample_dict.pop(i, "Bland"))
print("yes")
else:
print("No")

sample_dict["locatiom"]  = sample_dict.pop("city")

print(sample_dict)