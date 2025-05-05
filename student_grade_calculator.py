def calculate_grade(marks):
    a = sum(marks)/ len(marks)      # a means average
    if 100>= a>= 80 :           # 80-100 = A
        return a, "A"
    elif 79>= a >=60:           # 60-79 = B
        return a, "B"
    elif 59>= a>= 50:           # 50-59 = C
        return a, "C"
    elif 49>= a >= 41:          # 41-49 = D
        return a, "D"
    else:
        return a, "F"           # otherwise fail


# function for getting valid marks from user

def need_valid_mark(subject):    
    while True:
        try:
            mark = float(input("Enter marks for {subject} (0-100):"))
            if 0 <= mark <=100:        #checks if number is between 0 and 100
                return mark
            else:
                print("Error: Marks must be between 0 to 100")
        except ValueError:
            print("Error: Please enter a numeric value")


#another function for getting number of students  and subjects

def main():
    students =[]
    num_students = int(input("Enter the num of students : "))
    num_subjects = int(input("Enter the num of subjects :"))

    for _ in range(num_students):
        name = input("Enter students name: ")       # students name
        bg_name = input("Enter Background name: ")  # background name
        marks = []
        for j in range(num_subjects):
            subject_name = f"Subject {j+1}"
            mark = need_valid_mark(subject_name)    #
            marks.append(mark)

        a,grade = calculate_grade(marks)
        students.append({
            "name":name,
            "bg_name":bg_name,
            "marks":marks,
            "average": a,
            "grade" :grade
        })

    print("/n _____Students Result Report_____")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Background Name: {student['bg_name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")



if __name__ == "__main__":
    main()