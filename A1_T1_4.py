# if formula is T(K) = (T(°F) + 459.67)× 5/9
f = 72.50 # if temperature is

def F_2_K(f):
    k = (f + 459.67) * 5/9
    return k

l= F_2_K(f)
m= int(l)

print ("Fahrenheit of " + str (f) + " is " + str (m) + " in Kelvin. ")

# for this calculator the divice will not show a decimal value
# is easy to real.but if neet in line 10 change str(d) for: str (c)
