def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted:.2f}°F.")
    elif unit == "F":
        converted = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted:.2f}°C.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage:
convert_temperature()