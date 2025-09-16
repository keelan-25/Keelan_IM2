def convert_currency(dollar):
    rupee_rate = 88.07
    pound_rate = 0.73
    yuan_rate = 7.12

    rupee = dollar * rupee_rate
    pound = dollar * pound_rate
    yuan = dollar * yuan_rate
    print(f"{dollar:<12.2f}{rupee:<18.2f}{pound:<20}{yuan:<15.2f}")

while True:
    user_input = input("Enter dollar ($) (* to exit): ")

    if user_input == "*":
        print("Bye")
        break

    print("Dollar ($)  Indian Rupee (R)  British Pound (£)  China Yuan (¥)")

    numbers = user_input.split("@")

    for n in numbers:
        dollar = float(n)
        convert_currency(dollar)
