
import csv

# Task 1
def read_rows(path):
    """Return the rows of a CSV file as a list of dictionaries."""
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: the file '{path}' was not found.")
        return []


# Task A3
class Student:
    def __init__(self, student_id, name, programme, quiz, assignment, lab):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.quiz = quiz
        self.assignment = assignment
        self.lab = lab

    def average(self):
        return round(
            (self.quiz + self.assignment + self.lab) / 3, 1
        )

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    # Task B5 (Extension): Add __str__() so print(student)
    # shows the student's name, average, and grade.
    def __str__(self):
        return f"{self.name} - Average: {self.average():.1f} - Grade: {self.grade()}"


# Task B2
def build_students(rows):
    students = []

    for r in rows:
        students.append(
            Student(
                r["student_id"],
                r["name"],
                r["programme"],
                float(r["quiz"]),
                float(r["assignment"]),
                float(r["lab"])
            )
        )

    return students


# Task B3
def save_results(students, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "student_id", "name", "programme",
            "quiz", "assignment", "lab",
            "average", "grade"
        ])

        for s in students:
            writer.writerow([
                s.student_id,
                s.name,
                s.programme,
                s.quiz,
                s.assignment,
                s.lab,
                s.average(),
                s.grade()
            ])


def save_report(students, path):
    if not students:
        print("No student records available to create a report.")
        return

    best = max(students, key=lambda s: s.average())

    class_avg = round(
        sum(s.average() for s in students) / len(students), 1
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write("STUDENT RECORDS REPORT\n")
        f.write(f"Number of students: {len(students)}\n")
        f.write(f"Class average: {class_avg}\n")
        f.write(f"Top student: {best.name} ({best.average()})\n")


# Main program
if __name__ == "__main__":
    rows = read_rows("students.csv")
    print(len(rows), "records read")

    students = build_students(rows)

    if students:
        # Task B5 test: print each student's name, average, and grade.
        for student in students:
            print(student)

        save_results(students, "results.csv")
        save_report(students, "report.txt")

        print("Files created: results.csv and report.txt")
    else:
        print("No student records were processed.")


