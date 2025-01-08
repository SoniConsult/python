def Area_and_Perimeter():
    try:
        shape = input("Enter the shape: ").lower()

        if shape == "square":
            side = float(input("Enter the side length of the square: "))
            area = side * side
            perimeter = 4 * side
            print(f"Area of square: {area}, Perimeter of square: {perimeter}")

        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"Area of rectangle: {area}, Perimeter of rectangle: {perimeter}")

        elif shape == "parallelogram":
            base = float(input("Enter the base length of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            side = float(input("Enter the side length of the parallelogram: "))
            area = base * height
            perimeter = 2 * (base + side)
            print(f"Area of parallelogram: {area}, Perimeter of parallelogram: {perimeter}")

        elif shape == "triangle":
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            side1 = float(input("Enter the length of the first side: "))
            side2 = float(input("Enter the length of the second side: "))
            side3 = float(input("Enter the length of the third side: "))
            area = 0.5 * base * height
            perimeter = side1 + side2 + side3
            print(f"Area of triangle: {area}, Perimeter of triangle: {perimeter}")

        elif shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = 3.14159 * radius ** 2
            perimeter = 2 * 3.14159 * radius
            print(f"Area of circle: {area}, Perimeter of circle: {perimeter}")

        else:
            print("Invalid shape")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")


Area_and_Perimeter()


def calculate_statistics():
    try:
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        mode = statistics.mode(numbers) if len(set(numbers)) > 1 else "No mode"
        stdev = statistics.stdev(numbers) if len(numbers) > 1 else 0
        
        print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {stdev}")
        
    except ValueError:
        print("Please enter valid numbers.")
    except statistics.StatisticsError:
        print("Error in calculating mode or standard deviation.")

# Call the function
calculate_statistics()
 

 # question 3

def calculate_loan_payment():
    try:
        principal = float(input("Enter the principal amount: "))
        rate_of_interest = float(input("Enter the annual interest rate (in percentage): ")) / 100
        tenure = int(input("Enter the loan tenure in years: "))

        monthly_rate = rate_of_interest / 12
        months = tenure * 12

        if monthly_rate == 0:
            monthly_payment = principal / months
        else:
            monthly_payment = principal * monthly_rate * ((1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        
        print(f"Monthly payment: {monthly_payment:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate_loan_payment()


