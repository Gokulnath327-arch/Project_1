import numpy as np

subjects = ["Maths", "Physics", "Chemistry"]
students = {}

def enterdetails():
    print("\n--- Enter Student Details ---")
    ch = 'y'
    while ch.lower() == 'y':
        k = input("Enter name: ")
        try:
            m = int(input("Enter maths mark: "))
            p = int(input("Enter physics mark: "))
            c = int(input("Enter Chemistry mark: "))
        except ValueError:
            print("Invalid input! Please enter integer values for marks.")
            continue
            
        l = [m, p, c]
        students[k] = l
        ch = input("Enter another student detail? (y/n): ")

def average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

def selection_sort_desc(pairs):
    n = len(pairs)
    for i in range(n):
        biggest = i
        for j in range(i + 1, n):
            if pairs[j][1] > pairs[biggest][1]:    
                biggest = j
        pairs[i], pairs[biggest] = pairs[biggest], pairs[i]    
    return pairs

def linear_search(pairs, target_name):
    for index in range(len(pairs)):
        if pairs[index][0] == target_name:        
            return index
    return -1

def binary_search(sorted_names, target):
    low = 0
    high = len(sorted_names) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_names[mid] == target:
            return mid
        elif sorted_names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def display_rankings():
    if not students:
        print("\nNo student records found! Please enter details first.")
        return
    
    pairs = []                                        
    for name in students:
        avg = average(students[name])
        pairs.append((name, round(avg, 2)))

    ranking = selection_sort_desc(pairs)
    print("\n=== RANKING ===")
    for position, (name, avg) in enumerate(ranking, start=1):
        print(f"{position}. {name:<8} average = {avg:<6} grade = {get_grade(avg)}")

def perform_searches():
    if not students:
        print("\nNo student records found! Please enter details first.")
        return

    pairs = []
    for name in students:
        avg = average(students[name])
        pairs.append((name, round(avg, 2)))
    ranking = selection_sort_desc(pairs)

    print("\n=== SEARCHING ===")
    target_linear = input("Enter student name to perform Linear Search for: ")
    index = linear_search(ranking, target_linear)
    if index != -1:
        print(f"Linear search: {target_linear} is at rank {index + 1}")
    else:
        print(f"Linear search: {target_linear} not found in rankings.")

    names_in_order = sorted(students.keys())      
    target_binary = input("Enter student name to perform Binary Search for: ")
    index = binary_search(names_in_order, target_binary)
    if index != -1:
        print(f"Binary search: {target_binary} found at index {index} in {names_in_order}")
    else:
        print(f"Binary search: {target_binary} not found.")

def display_numpy_stats():
    if not students:
        print("\nNo student records found! Please enter details first.")
        return

    marks = np.array(list(students.values()))
    student_names = list(students.keys())

    print("\n=== SUBJECT STATISTICS (NumPy) ===")
    subject_avg = np.mean(marks, axis=0)          
    subject_max = np.max(marks, axis=0)
    subject_std = np.std(marks, axis=0)          
    topper_index = np.argmax(marks, axis=0)        

    for i in range(len(subjects)):
        print(f"{subjects[i]:<10} mean = {subject_avg[i]:.1f}  "
              f"max = {subject_max[i]}  spread = {subject_std[i]:.1f}  "
              f"topper = {student_names[topper_index[i]]}")

    best_subject = subjects[int(np.argmax(subject_avg))]
    weakest_subject = subjects[int(np.argmin(subject_avg))]
    print(f"\nClass is strongest in {best_subject} and weakest in {weakest_subject}.")

    overall_mean = np.mean(marks)
    print(f"Overall mean = {overall_mean:.1f}. Students needing support:")
    
    # Compute rankings to check support needed
    pairs = [(name, average(students[name])) for name in students]
    ranking = selection_sort_desc(pairs)
    for name, avg in ranking:
        if avg < overall_mean:
            print(" -", name)

def main():
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM  ")
        print("==============================")
        print("1. Enter Student Details")
        print("2. View Student Rankings")
        print("3. Search Students (Linear/Binary)")
        print("4. View Subject Statistics (NumPy)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            enterdetails()
        elif choice == '2':
            display_rankings()
        elif choice == '3':
            perform_searches()
        elif choice == '4':
            display_numpy_stats()
        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
