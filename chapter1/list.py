ls = []

ls.append(1)
ls.append(2)

for i in range(2,6):
    ls.append(i)

print(ls)
for i in ls:
    print(i)

first = ls[0]
last = ls[-1]

print(f"first is {first}, last is {last}")