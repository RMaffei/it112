
"""
Prompt the user to input a temperature in Fahrenheit. Compute the 
temperature in Celsius and Kelvin. Display the results.
"""

### Ask the user to input a Farenheit temperature

F=input("Input a Farenheit temperature:")
F=float(F)

# print(F)

### Compute the temperature in Celsius and Kelvin

C=(F-32) * 5/9 
K=5 * (F-32)/9 + 273.15 

### Display the results

print("The Farenheit temperature is " + str(F))
print("The temperature in Celsius is " + str(C))
print("The temperature in Kelvin is " + str(K))
