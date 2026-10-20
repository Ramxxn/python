
n = int(input("Enter pattern number: "))


# pattern 1
for i in range (1, n+1):
    print(" " * (n-i), end="")
    print("*" * ((i*2)-1), end="")
    print("")




print("\n")
# pattern 2
for i in range (1, n+1):
    print("*" * i, end="")
    print("")




print("\n")
# pattern 3
for i in range (1, n+1):
    if i == 1 or i == n:
        print("*" * n, end="")
        print("")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
        print("")
        

