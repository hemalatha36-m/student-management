students = []  # global list to store students


def add_student():
    roll = input("Roll no: ").strip()
    # Check duplicate roll no
    if any(s['roll_no'] == roll for s in students):
        print("❌ Roll no already exists.")
        return
    
    name = input("Name: ").strip()
    grade = input("Grade: ").strip()
    age = input("Age: ").strip()

    students.append({
        "roll_no": roll,
        "name": name,
        "grade": grade,
        "age": age
    })
    print("✅ Student added successfully.")


def view_students():
    if not students:
        print("⚠️ No students found.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll_no']}, Name: {s['name']}, Grade: {s['grade']}, Age: {s['age']}")


def search_student():
    roll = input("Enter roll no to search: ").strip()
    for s in students:
        if s['roll_no'] == roll:
            print(f"✅ Found: Roll: {s['roll_no']}, Name: {s['name']}, Grade: {s['grade']}, Age: {s['age']}")
            return
    print("❌ Student not found.")


def update_student():
    roll = input("Enter roll no to update: ").strip()
    for s in students:
        if s['roll_no'] == roll:
            print("Leave blank to keep old value.")
            name = input(f"New Name ({s['name']}): ").strip()
            grade = input(f"New Grade ({s['grade']}): ").strip()
            age = input(f"New Age ({s['age']}): ").strip()

            if name: 
                s['name'] = name
            if grade: 
                s['grade'] = grade
            if age: 
                s['age'] = age

            print("✅ Student updated successfully.")
            return
    print("❌ Student not found.")


def delete_student():
    roll = input("Enter roll no to delete: ").strip()
    for s in students:
        if s['roll_no'] == roll:
            students.remove(s)
            print("✅ Student deleted successfully.")
            return
    print("❌ Student not found.")


def main():
    while True:
        print("\n=== Student Management System ===")
        print("1) Add  2) View  3) Search  4) Update  5) Delete  6) Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
