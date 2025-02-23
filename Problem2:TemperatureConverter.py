temp_convert_from = input("Which scale are you converting from? (C/F/K) ")

while temp_convert_from != "C" and temp_convert_from != "F" and temp_convert_from != "K":
    print("You entered an unrecognized temperature scale, please try again.")
    temp_convert_from = input("Which scale are you converting from? (C/F/K) ")

temp_convert_to = input("Which scale are you converting to? (C/F/K) ")
while temp_convert_to != "C" and temp_convert_to != "F" and temp_convert_to != "K":
    print("You entered an unrecognized temperature scale, please try again.")
    temp_convert_to = input("Which scale are you converting from? (C/F/K) ")

try:
    temp = float(input("Enter the temperature in " + temp_convert_from + ": "))

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

    print(f"{temp}° {temp_convert_from} is {new_temp}° {temp_convert_to}")
    
except(ValueError):
    print("You entered a non-numerical value.")
