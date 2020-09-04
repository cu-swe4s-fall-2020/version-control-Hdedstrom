import math_lib as ml

#Find the sum of 2 and 3. 
my_sum = ml.add(2,3)

#Divide 6 and 2. 
my_division = ml.div(6,2)

#Show that the error message for the div function works. 
illegal_attempt = ml.div(6,0)

return "my_sum = 2 + 3 = " + str(my_sum)
return "my_division = 6 / 2 = " + str(my_division)
return "illegally divide 6: " + str(illegal_attempt)
