def calculate_results(marks: list) -> dict:
    if not marks:
        return {"total": 0, "average": 0.0}
    numeric_marks = [float(mark) for mark in marks]
    total = sum(numeric_marks)
    average = total / len(numeric_marks)
    return {"total": total, "average": round(average, 2)}

if __name__ == "__main__":
    print("--- Student Marks Calculator (Push 1 Baseline) ---")
    try:
        user_input = input("Enter student marks separated by spaces: ")
        student_marks = [float(x) for x in user_input.split() if x.strip()]
        results = calculate_results(student_marks)
        print(f"Total Marks:   {results['total']}")
        print(f"Average Marks: {results['average']}")
    except ValueError:
        print("Error: Please enter valid numbers only.")
