# a + b problem

a = 1
b = 2
c = input()

result = a + b + c
print(result)

# is the result greater than 10?
if result > 10:
    print("greater than 10")
elif result <=0:
    print("less than 0")
else:
    print("less than 10")

for i in range(5):
    print(f"i is {i}, i*i is {i*i}")