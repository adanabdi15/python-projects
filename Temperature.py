
#hw6
#Adan Abdi


#This function prints one line of conversion table
def print_table_line(celsius):
#Calculate the Fahrenheit temperature using the formula 
    fahrenheit = round(celsius * 9 / 5 + 32)
#Print the Celsius and Fahrenheit Values.
    print(f"{celsius:<7}\t{fahrenheit}")
#This function prints the entire converison table
def print_conversion_table(min_temp, max_temp):
#Print the header for the table
    print("Celsius\tFahrenheit"
#prints the dashes under the header
    print("------------------")
#Loop through all the celsius temperatures
    for celsius in range(min_temp, max_temp + 1):
#Print one line of the table for each celsius value 
        print_table_line(celsius)

#Main program part of the script 
min_temp = int(input("Please enter the starting temperature for the table: "))
max_temp = int(input("Please enter the ending temperature for the table: "))
print()
print_conversion_table(min_temp, max_temp)
