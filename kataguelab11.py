gradelist = []
passers = 0

while True:
    x = input("Enter the student grade (or type 'Done' to finish): ")

    if x.lower() == 'done':  
        break

    
    if x.isdigit():
        x = int(x)
        if x < 40 or x > 100:
            print("Invalid grade, the grade must be between 40 and 100.")
        else:
            gradelist.append(x)
            if x >= 75:
                passers += 1
    else:
        print("Please enter a valid number.")

if gradelist:
    sum_grades = sum(gradelist)
    average = sum_grades / len(gradelist)
    percent_passers = (passers / len(gradelist)) * 100

    print(f"Average grade between all students: {average:.2f}")
    print(f"Passers: {passers}")
    print(f"Pass rate: {percent_passers:.2f}%")
    print(f"Grades entered: {gradelist}")
else:
    print("No valid grades were entered.")
