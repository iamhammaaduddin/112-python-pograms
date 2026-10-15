# Problem 003: Calculate simple interest given P, R, T → (P × R × T) / 100

p = float(input("Enter principal (P): "))
r = float(input("Enter rate (R): "))
t = float(input("Enter time (T) in years: "))
si = (p * r * t) / 100
print("Simple Interest:", si)
