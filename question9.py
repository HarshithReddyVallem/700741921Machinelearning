N = int(input("Enter the no. of Students :"))
Weight_in_lbs = []
Weight_in_Kgs = []
print(" Enter weight of  Students")
for i in range(N):
    #assigning weights in lbs to temp
    temp = int(input(str(i+1)+ "Student weight :"))
    Weight_in_lbs.append(temp)
    # 1lb = 0.453592 kg
    Weight_in_Kgs.append(float("{:2f}".format(temp*0.453592)))
print(" weight in lbs : ", Weight_in_lbs)
print(" weight in kgs : ", Weight_in_Kgs)