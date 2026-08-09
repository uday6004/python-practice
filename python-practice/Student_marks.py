student_count = int(input("Enter the number of students: "))
marks = []

# Read and store all marks using append()
for _ in range(student_count):
    marks.append(int(input()))

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update mark at 0-based index with bounds check
if 1 <= position <= len(marks):
    marks[position - 1] = corrected_mark
else:
    print(f"Error: Position {position} is out of range. Valid range is 1 to {len(marks)}.")


# Calculate required statistics
total_marks = sum(marks)
average_marks = total_marks / student_count
highest_mark = max(marks)
lowest_mark = min(marks)

# Count passed students
passed_count = 0
for mark in marks:
    if mark >= passing_mark:
        passed_count += 1

# Display results exactly as required
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Students: {passed_count}")