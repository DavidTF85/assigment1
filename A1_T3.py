temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
# Values measured in degrees

maximum = 0
minimum = 0
i = 0
# maximum calculation
while i < len(temperatures_arr):
    temperature = temperatures_arr[i]
    i = i + 1
    if temperature > maximum:
        maximum = temperature
print ("The maximum temperature is", maximum , "degrees.")

# Minimum calculation
i = 0
minimum = maximum
while i < len(temperatures_arr):
    temperature = temperatures_arr[i]
    i = i + 1
    if temperature < minimum:
        minimum = temperature
print("The minimum temperature is", minimum, "degrees.")

# this will show the minimum value in the array
