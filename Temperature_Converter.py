# Welcome Note
print("Howdy, I'm Prabindh")
# Selecion Of Options
print("\nA. Celsius To Farenheit \nB. Farenheit To Celsius")
# Note For Selecion
option=input("\nEnter You Option For Temperature Conversion : ").lower()
# Declaring Variables
# Option A
if (option=="a"):
    celsius1 = float(input("Enter Temperature in Celsius: "))
    fahrenheit1 = 9.0/5.0 * celsius1 + 32
    print("Temperature:", celsius1, "Celsius = ", fahrenheit1, " Fahrenheit")
# Option B
if (option=="b"):
    fahrenheit2 = float(input("Enter Temperature in Fahrenheit: "))
    celsius2 = (fahrenheit2 - 32) * 5.0/9.0
    print("Temperature:", fahrenheit2, "Fahrenheit = ", celsius2, " Celsious")