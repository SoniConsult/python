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
