def save_student_data():
    filename = 'Marks.data'
    num_students = int(input("Enter the number of students: "))

    with open(filename, 'w') as file:
        for i in range(num_students):
            print(f"\nEnter details for student {i + 1}:")
            roll_no = input("Roll Number: ")
            name = input("Name: ")
            marks = input("Marks: ")
            # Format: roll_no,name,marks
            file.write(f"{roll_no},{name},{marks}\n")

    print(f"\nStudent details saved to '{filename}'.")

# Run the function
save_student_data()
