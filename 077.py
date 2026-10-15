# Problem 077: Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order.

def show(i, n):
    if i > n:
        return
    print(i, end=" ")      # printed while going forward (increasing)
    show(i + 1, n)
    print(i, end=" ")      # printed while coming back (decreasing)


n = int(input("Enter N: "))
show(1, n)
print()
