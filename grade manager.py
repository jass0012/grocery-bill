class GradebookManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self):
        print("\nAdd Student Information")
        name = input("Enter student name: ")
        
        if name in self.students:
            print(f"Student {name} already exists in the gradebook.")
            return
        
        try:
            math = float(input("Enter Math score 0-100: "))
            science = float(input("Enter Science score 0-100: "))
            english = float(input("Enter English score 0-100: "))
            
            if not (0 <= math <= 100 and 0 <= science <= 100 and 0 <= english <= 100):
                print("Scores must be between 0 and 100.")
                return
                
            self.students[name] = {
                'math': math,
                'science': science,
                'english': english,
                'average': (math + science + english) / 3
            }
            print(f"Student {name} added successfully")
            
        except ValueError:
            print("Invalid input. Please enter numeric values for scores")
    
    def calculate_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 75:
            return 'B'
        elif average >= 60:
            return 'C'
        elif average >= 50:
            return 'D'
        else:
            return 'F'
    
    def display_all_students(self):
        if not self.students:
            print("\nNo students in the gradebook")
            return
            
        print("\nStudent Gradebook")
        print("Name                Math      Science   English   Average   Grade")
        
        for name, scores in self.students.items():
            grade = self.calculate_grade(scores['average'])
            print(f"{name:<20}{scores['math']:<10.1f}{scores['science']:<10.1f}"
                  f"{scores['english']:<10.1f}{scores['average']:<10.1f}{grade:<6}")
    
    def search_student(self):
        name = input("\nEnter student name to search: ")
        
        if name in self.students:
            scores = self.students[name]
            grade = self.calculate_grade(scores['average'])
            
            print("\nStudent Details")
            print(f"Name: {name}")
            print(f"Math: {scores['math']}")
            print(f"Science: {scores['science']}")
            print(f"English: {scores['english']}")
            print(f"Average: {scores['average']:.1f}")
            print(f"Grade: {grade}")
        else:
            print(f"Student {name} not found in the gradebook")
    
    def run(self):
        while True:
            print("\nStudent Gradebook Manager")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Exit")
            
            choice = input("Enter your choice 1-4: ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                print("Exiting Gradebook Manager")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4")

if __name__ == "__main__":
    gradebook = GradebookManager()
    gradebook.run()