power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2]
#median is the number in the mitddle of a data scoreprint
#how ever if there is 2 numbers it have to be sum and then devide by 2
#so if x,y are in the middle of a odd number of data set
# the median will be x+y/2=median
middle_value = float(len(power_arr))/2
return (power_arr[int(middle)]


middle_value = 0
if(a%2==0):
    print("This Number is Even")
    x, y = find_middle(power_arr)
    middle_value = (x + y) / 2

else:
    print("This Number is Odd")
    middle_index = float(len(power_arr))/2
    print("The middle index is", middle_index)
    middle_value = power_arr[int(middle_index - .5)]
