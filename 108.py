# Problem 108: Right arrow pattern

size = 5
mid = size // 2

for r in range(size):
    for c in range(size):
        distance = abs(r - mid)
        if distance == 0 or c == mid or (distance == 1 and c == mid + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
