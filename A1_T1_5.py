# if formula is T(°C) = T(K) - 273.15
#check here URL: https://www.rapidtables.com/convert/temperature/

k = 300.00 # if temperature is

def k_2_c(k):
    c = k - 273.15
    return c

c= k_2_c(k)
b= int(c)
print ("Kelvin of " + str (k) +  " is " + str (b) + " in Celsius. ")

# for this calculator the divice will not show a decimal value
# is easy to real. but if need in line 10 change str(b) for: str (c)
