c= 25.0

def K_2_C(c):
    # kalving formula = T(K) = T(°C) + 273.15
    k = c+273.5
    return k

f= K_2_C(c)

print ("Celcius of " + str(c) + " is "+ str(f) + " in Kalvin.")
