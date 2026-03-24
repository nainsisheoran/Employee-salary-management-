👨‍💼 Employee Management System using OOP in Python
 📌 Description
This project is a simple Employee Management System built using Object-Oriented Programming (OOP) concepts in Python.  
It allows users to input details of employees and managers, and calculates the total salary for managers including bonus.

 🎯 Features
- Add employee details (name, ID, salary)
- Add manager details (name, ID, salary, bonus)
- Display employee information
- Calculate and display manager total salary (salary + bonus)

🧠 Concepts Used
- Classes and Objects
- Inheritance
- Constructors (`__init__`)
- Method Calling
- Code Reusability

🏗️ Project Structure
- `Employee` (Base Class)
  - Attributes: name, id, salary
  - Method: display_employee()

- `Manager` (Derived Class)
  - Inherits from Employee
  - Additional attribute: bonus
  - Methods:
    - total_salary()
    - display_Manager()

🛠️ Technologies Used
- Python (Core Python)
- Object-Oriented Programming (OOP)

▶️ How to Run

1. Make sure Python is installed
2. Download or clone the repository
3. Open terminal and navigate to the project folder
4. Run the program:

```bash
python Employee_management_system.py
