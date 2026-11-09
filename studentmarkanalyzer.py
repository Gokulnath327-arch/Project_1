
import numpy as np

subjects = ["Maths", "Physics", "Chemistry"]          

students = {                                          
    "Aarav": [78, 85, 90],
    "Diya": [92, 88, 95],
    "Karthik": [65, 70, 58],
    "Meena": [88, 91, 84],
    "Rahul": [45, 52, 60],
    "Sneha": [99, 94, 97],
}



def average(marks):
    """Average using a plain loop (no library)."""
    total = 0
    for m in marks:
        total += m
    return total / len(marks)


def get_grade(avg):
    """Convert an average mark into a grade using if / elif / else."""
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def selection_sort_desc(pairs):
    """Sort a list of (name, average) tuples from highest to lowest."""
    n = len(pairs)
    for i in range(n):
        biggest = i
        for j in range(i + 1, n):
            if pairs[j][1] > pairs[biggest][1]:   
                biggest = j
        pairs[i], pairs[biggest] = pairs[biggest], pairs[i]   
    return pairs


def linear_search(pairs, target_name):
    """Check every item one by one. Returns its position or -1."""
    for index in range(len(pairs)):
        if pairs[index][0] == target_name:        
            return index
    return -1


def binary_search(sorted_names, target):
    """Search a SORTED list by repeatedly halving it."""
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


def main():
    pairs = []                                    
    for name in students:
        avg = average(students[name])
        pairs.append((name, round(avg, 2)))

    ranking = selection_sort_desc(pairs)
    print("=== RANKING ===")
    for position, (name, avg) in enumerate(ranking, start=1):
        print(f"{position}. {name:<8} average = {avg:<6} grade = {get_grade(avg)}")

    print("\n=== SEARCHING ===")
    index = linear_search(ranking, "Meena")
    print("Linear search: Meena is at rank", index + 1)

    names_in_order = sorted(students.keys())      
    index = binary_search(names_in_order, "Rahul")
    print("Binary search: Rahul found at index", index, "in", names_in_order)


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
    for name, avg in ranking:
        if avg < overall_mean:
            print(" -", name)

if __name__ == "__main__":
    main()
