pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]
#= ( Σ xi ) / n= sume of #/ by the amount of the  data set
x= len (pressure_arr)
i= int (x)
print (str(i) + " is the length of the data set.")

y= sum (pressure_arr)
z= int (y)
print(str(z)+ " is the sum value of the numbers in the data set.")

mean = y / x
h= int(mean)
print ( str(h) + " is the mean (average) of the data.")
