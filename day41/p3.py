#display the student marks reports 
#student grade is distinction provided total marks range from 300 and 250
# "" dtusent grade is forst provided total marks range from 249 and 200
#student grade is second provided total marks range from 199 and 150
# student grade is third provided total marks range from 149 and 100
# student grade is fail provided total marks range from 99 and below
# student marks report is provided total marks range from 300 and below
while True:
    total_marks = int(input("Enter the total marks (0-300): "))
    if 0 <= total_marks <= 300:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 300.")
        
if total_marks >= 250:
    print("Student grade: Distinction")
elif total_marks >= 200:
    print("Student grade: First Division")
elif total_marks >= 150:
    print("Student grade: Second Division")
elif total_marks >= 100:
    print("Student grade: Third Division")
else:
    print("Student grade: Fail")
    