# An employee’s total weekly pay equals the hourly wage multiplied by 
# the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime 
# hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, 
# total regular hours, and total overtime hours and displays an employee’s total weekly pay.


def calcWeekly(hourlyWage, regHours, otHours):
    overtime_rate = 1.5 * hourlyWage  
    regular_pay = hourlyWage * regular_hours  
    overtime_pay = overtime_rate * otHours  
    total_pay = regular_pay + overtime_pay  
    return total_pay

if __name__ == "__main__":
    print("--- Employee Weekly Pay Calculator ---")
    try:

        hourlyWage = float(input("Enter the hourly wage: "))
        regular_hours = float(input("Enter the total number of regular hours: "))
        otHours = float(input("Enter the total number of overtime hours: "))

        if hourlyWage < 0 or regular_hours < 0 or otHours < 0:
            print("Error: Hours and wage must be non-negative.")
        else:

            total_pay = calcWeekly(hourlyWage, regular_hours, otHours)
            print(f"The employee's total weekly pay is: ${total_pay:.2f}")
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
