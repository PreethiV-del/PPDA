def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C, F, or K): ").upper()

    print("Convert to:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = input("Enter choice (1/2/3): ")

    if unit == 'C':
        if choice == '1':
            print(f"{temp} C is {temp} C")
        elif choice == '2':
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp} C is {fahrenheit} F")
        elif choice == '3':
            kelvin = temp + 273.15
            print(f"{temp} C is {kelvin} K")
        else:
            print("Invalid conversion choice.")

    elif unit == 'F':
        if choice == '1':
            celsius = (temp - 32) * 5/9
            print(f"{temp} F is {celsius} C")
        elif choice == '2':
            print(f"{temp} F is {temp} F")
        elif choice == '3':
            kelvin = (temp - 32) * 5/9 + 273.15
            print(f"{temp} F is {kelvin} K")
        else:
            print("Invalid conversion choice.")

    elif unit == 'K':
        if choice == '1':
            celsius = temp - 273.15
            print(f"{temp} K is {celsius} C")
        elif choice == '2':
            fahrenheit = (temp - 273.15) * 9/5 + 32
            print(f"{temp} K is {fahrenheit} F")
        elif choice == '3':
            print(f"{temp} K is {temp} K")
        else:
            print("Invalid conversion choice.")

    else:
        print("Invalid unit input.")

temperature_converter()
