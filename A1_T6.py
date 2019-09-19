import statistics

JD_data = [10, 20, 50, 60, 100, 32, 7, 50, 99, 50 ]
#mode
mod =statistics.mode(JD_data)
print (mod, "is the mode in the data set" )
# print starndart deviation
stdev = statistics.stdev(JD_data)
print("The standart dDeviation of the sample is" , stdev)

# variance calculation
var= statistics.variance(JD_data)
print("Variance of sample set is" , var)


#range
print(len(JD_data), "is the range of the data set")

#variance
variance = statistics.variance(JD_data)
print(variance, "is the variance of the data set")
