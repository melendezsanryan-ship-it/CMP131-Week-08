
store=int(input("enter number of store"))

print("\nsales bar chart")
print("Each * represents $100\n")

for i in range(store):
    ast=""
    sale=int(input("Enter today's sales for store" + str(int)+ ":"))
    while sale<0:
        sale=int(input("Error: Sales cannot be negative:"))    
    for j in range(sale//100) :
        ast=ast+"*"

    ast= ast + "\n"

print(ast)


