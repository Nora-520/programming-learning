import json
import os

def save_students(students):
    with open("students.json","w") as file:
        json.dump(students,file)
    print(os.getcwd())

def load_students():
    try:
        with open("students.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_student(students):
    while True:
        name = input("student name:").strip()
        if len(name) == 0:
            print("Error.")
        else:
            break
    while True:
        try: 
            score = int(input("student score:"))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score.Please enter a number.")
    students[name] = score

def show_student(students):
    print(f"{"Name":<15}{"Score":>5}")
    print("-"*20)
    for name,score in students.items():
        print(f"{name:<15}{score:>5}")

def calculate_average(students):
    total = 0
    if len(students) == 0:
        print("No students data.")
    else:
        for score in students.values():
            total += score
            averageScore = total/len(students)
        print("========================")
        print("Average Score".center(24))
        print("========================")
        print(f"Average score:{averageScore:.2f}")

def find_highest(students):
    highest_score = 0
    highest_name = ""
    if len(students) == 0:
        print("No students data.")
    else:
        for name,score in students.items():
            if score > highest_score:
                highest_score = score
                highest_name = name
        print("========================")
        print("Highest Score".center(24))
        print("========================")
        print(highest_name,":",highest_score)

students = load_students()

while True:
    print("========================")
    print("Student Manager".center(24))
    print("========================")
    print("1.Add student")
    print("2.Show student")
    print("3.Calculate the average")
    print("4.The highest score")
    print("5.Exit")

    choice = input("Please choose:")

    if choice == "1":
        add_student(students)
        save_students(students)

    elif choice == "2":
        show_student(students)

    elif choice == "3":
        calculate_average(students)
        
    elif choice == "4":
        find_highest(students)

    elif choice == "5":
        print("Program exit.")
        break

    else:
        print("Invalid option.")


