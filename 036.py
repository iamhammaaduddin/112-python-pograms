# Problem 036: Read the cost price and selling price — print profit, loss, or no profit no loss

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit of", sp - cp)
elif cp > sp:
    print("Loss of", cp - sp)
else:
    print("No profit, no loss")
