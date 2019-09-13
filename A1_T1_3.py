# if formula Fahrenheit to Celsius is: T(°C) = (T(°F) - 32) × 5/9
f= 80.00  # if temperature is

def F_2_C(f):
    c = (f-32) *5/9
    return c
c = F_2_C(f)
d = int (c)

print("Fahrenheit of " + str (f) + " is " +  str(d) + " in Celsius. ")

# for this calculator the divice will not show a decimal value
# is easy to real.but if need in line 10 change str(d) for: str (c)
