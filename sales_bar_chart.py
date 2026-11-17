def main():
    store = int(input("Enter number of stores: "))

    while store <= 0:
        if store <= 0:
            print("Error: Number of stores must be greater than 0.")
            store = int(input("Enter number of stores: "))

    print()
    print("SALES BAR CHART")
    print("(Each * = $100)")
    print()

    for i in range(1, store + 1):
        sale = int(input("Enter today's sales for store " + str(i) + ": "))

        while sale < 0:
            if sale < 0:
                print("Error: Sales cannot be negative.")
                sale = int(input("Enter today's sales for store " + str(i) + ": "))

        num_stars = sale // 100 #assigning variable num_stars as number of stars

        stars = "" 
        for j in range(num_stars): 
            stars = stars + "*"

        print("Store " + str(i) + ": " + stars) 


main()
