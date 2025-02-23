# get input by prompting for scale that the temperature will be converted from
temp_convert_from = input("Which scale are you converting from? (C/F/K) ")

# checks to see if the input matches one of the allowed scales (C/F/K), if it doesn't it will keep prompting the user for a valid scale
while temp_convert_from != "C" and temp_convert_from != "F" and temp_convert_from != "K":
    print("You entered an unrecognized temperature scale, please try again.")
    temp_convert_from = input("Which scale are you converting from? (C/F/K) ")

# get input by prompting for scale that the temperature will be converted to
temp_convert_to = input("Which scale are you converting to? (C/F/K) ")

# checks to see if the input matches one of the allowed scales (C/F/K), if it doesn't it will keep prompting the user for a valid scale
while temp_convert_to != "C" and temp_convert_to != "F" and temp_convert_to != "K":
    print("You entered an unrecognized temperature scale, please try again.")
    temp_convert_to = input("Which scale are you converting from? (C/F/K) ")

# if no errors occur it will run this code
try:
    # converts the users input from a string to a float and sets it to the variable temp
    temp = float(input("Enter the temperature in " + temp_convert_from + ": "))

    # if statements that check the scale that the temperature is in and will be converted to to complete the appropriate conversion
    if(temp_convert_from == "C" and temp_convert_to == "F"):
        new_temp = (temp * 1.8) + 32

    if(temp_convert_from == "F" and temp_convert_to == "C"):
        new_temp = (temp - 32) * (5/9)

    if(temp_convert_from == "K" and temp_convert_to == "C"):
        new_temp = temp - 273.15

    if(temp_convert_from == "C" and temp_convert_to == "K"):
        new_temp = temp + 273.15

    if(temp_convert_from == "K" and temp_convert_to == "F"):
        new_temp = (temp - 273.15) * 1.8 + 32

    if(temp_convert_from == "F" and temp_convert_to == "K"):
        new_temp = (temp - 32) * (5/9) + 273.15

    # prints the converted temperature
    print(f"{temp}° {temp_convert_from} is {new_temp}° {temp_convert_to}")
    
# if the user enters anything other than a number for the temperature, it handles the error by simply printing a message of what went wrong
except(ValueError):
    print("You entered a non-numerical value.")
