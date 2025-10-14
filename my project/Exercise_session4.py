midterm = float(input("Enter your midterm score:"))
final = float(input("Enter your final score:"))
average = (midterm + final)/2
if (0 <= midterm <= 20) and (0 <= final <=20) and (average >= 10):
    print("Average:", average , "=>passed")
elif (0 <= midterm <= 20) and (0 <= final <=20) and (average < 10): 
    print("Average:", average , "=>failed")
else:
    print("Error:", "scores are not defined")


