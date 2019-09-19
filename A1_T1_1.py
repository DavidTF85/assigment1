def C_to_F(c):
    f = (c * 9/5) + 32
    # convertion formula is:T(°F) = T(°C) × 9/5 + 32
    #check here URL: https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
    return f

c = 35.46
f = C_to_F(c)
print ("Celcius of "  +  str (c)  +  " is "  +  str (f) + " in Fahrenheit")
