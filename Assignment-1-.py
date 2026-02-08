#Take Student Information 
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

subject1 = float(input("Enter marks of Subject-1: "))
subject2 = float(input("Enter marks of Subject-2: "))
subject3 = float(input("Enter marks of Subject-3: "))

#store the data

student_infos = [name,age,subject1,subject2,subject3]
marks = [subject1,subject2,subject3]

#calculate result

total_marks = subject1+subject2+subject3
average = total_marks/3

print("\nTotal Marks:", total_marks)
print(f"Average Marks: {average:.2f}")

if average >= 40:
    print("Result: Pass")
else:    
    print("Result: Fail")

#Simple String Operations

print('\nName in Uppercase:', name.upper())
print('Name in Lowercase:', name.lower())
print('Reversed Name:', name[::-1])

#simple list operations

student_infos.append(f'Average is {average:.2f}')
print("\n Latest Student Information:", student_infos)