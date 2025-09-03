while True:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows == 0 or cols == 0:
        print("Invalid input.")
        break

    search_val = int(input("Enter a number to search in the table: "))

    print("\nMultiplication Table:")
    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            product = x * y
            if product == search_val:
                print("{" + str(product) + "}", end="\t")
            else:
                print(product, end="\t")
        print()
    print()
