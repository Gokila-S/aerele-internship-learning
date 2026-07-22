def process_marks(marks):
    total = 0
    for m in marks:
        total += m

    avg = total / len(marks)

    if avg >= 50:
        print("Pass")
    else:
        print("Fail")