"""
GradeBook Analyzer
Name: Jitesh Kumar
Roll no: 2501010180
Project - Programming for Problem Solving Using Python
"""

import csv

def menu():
    print("\n--- GradeBook Analyzer ---")
    print("1. Enter student marks manually")
    print("2. Load marks from CSV file")
    print("3. Exit")

# ---------------- INPUT METHODS ----------------

def manual_input():
    marks = {}
    n = int(input("How many students? : "))
    for i in range(n):
        name = input("Student name: ")
        score = int(input("Marks: "))
        marks[name] = score
    return marks

def load_csv():
    marks = {}
    file = input("Enter CSV file name: ")
    try:
        with open(file) as f:
            r = csv.reader(f)
            next(r)
            for row in r:
                marks[row[0]] = int(row[1])
    except:
        print("File error!")
    return marks

# ---------------- STATISTICS ----------------

def average(m):
    return sum(m.values()) / len(m)

def median(m):
    s = sorted(m.values())
    n = len(s)
    if n % 2 != 0:
        return s[n//2]
    else:
        return (s[n//2] + s[n//2 - 1]) / 2

def max_score(m):
    name = max(m, key=m.get)
    return name, m[name]

def min_score(m):
    name = min(m, key=m.get)
    return name, m[name]

# ---------------- GRADES ----------------

def make_grades(m):
    g = {}
    for name, score in m.items():
        if score >= 90:
            g[name] = "A"
        elif score >= 80:
            g[name] = "B"
        elif score >= 70:
            g[name] = "C"
        elif score >= 60:
            g[name] = "D"
        else:
            g[name] = "F"
    return g

def grade_count(g):
    d = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for v in g.values():
        d[v] += 1
    return d

# ---------------- PASS / FAIL ----------------

def pass_fail(m):
    passed = [n for n, s in m.items() if s >= 40]
    failed = [n for n, s in m.items() if s < 40]
    return passed, failed

# ---------------- TABLE ----------------

def print_table(m, g):
    print("\n--- Final Result Table ---")
    print("Name\t\tMarks\tGrade")
    print("-------------------------------")
    for name in m:
        print(f"{name}\t\t{m[name]}\t{g[name]}")

# ---------------- MAIN PROGRAM ----------------

def main():
    print("Welcome to GradeBook Analyzer!")

    while True:
        menu()
        ch = input("Choose option: ")

        if ch == '1':
            marks = manual_input()
        elif ch == '2':
            marks = load_csv()
        elif ch == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            continue

        if len(marks) == 0:
            print("No data available!")
            continue

        # --------- Analysis ---------
        avg = average(marks)
        med = median(marks)
        mx_n, mx_s = max_score(marks)
        mn_n, mn_s = min_score(marks)

        print("\n--- Summary ---")
        print("Average:", round(avg, 2))
        print("Median:", med)
        print("Highest:", mx_n, mx_s)
        print("Lowest :", mn_n, mn_s)

        grades = make_grades(marks)
        dist = grade_count(grades)

        print("\nGrade Distribution:", dist)

        passed, failed = pass_fail(marks)
        print("\nPassed:", passed)
        print("Failed:", failed)

        print_table(marks, grades)

        again = input("\nRun again? (y/n): ")
        if again.lower() != 'y':
            break

main()
