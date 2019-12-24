## Chapter 02 | Exercise 05
# Write a program which prompts the user for a Celsius temperature, convert the
# temperature to Fahrenheit, and print out the converted temperature.


print("Celsius to Fahrenheit Calculator v1.0")

## QUESTIONS
#  What's best practice for formatting variable names?
#  What's best method to restrict acceptable input responses to control data quality?
Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = Celsius * 1.8 + 32

print(f"{Celsius} degrees Celsius converts to {Fahrenheit} degrees Fahrenheit")
