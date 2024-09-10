import random
print("This is a Test")


print("new")

print("this is the second test")

print("This is a test from the code space side")
num = random.randint(0,25)
if (num % 2) == 1:
    print("num is even")
else:
    print("Num is odd")
while True:
    g = int(input("pick a number: "))
    if g == num:
        print("you won")
        break
    else:
        print("Your wrong try again")