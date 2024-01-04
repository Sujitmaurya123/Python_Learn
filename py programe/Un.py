#a =int(input())
#b = int(input())
# print(a//b)
# print((a)/(b))
n = int(input())
if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0 and 2 <= n <= 5):
    print("NOT Weird")
elif (n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
else:
    print("NOT Weird")
