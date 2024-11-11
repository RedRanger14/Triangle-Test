def classify_triangle(angle1, angle2, angle3):
    # Check if the angles form a valid triangle
    if angle1 + angle2 + angle3 != 180:
        return "Not a triangle"
    
    # Classify the triangle
    if angle1 == angle2 == angle3:
        triangle_type = "Equilateral"
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    # Determine the subtype of the triangle
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        subtype = "Acute"
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        subtype = "Right-angled"
    else:
        subtype = "Obtuse"
    
    return f"{triangle_type} and {subtype}"

def get_valid_angle(prompt):
    while True:
        try:
            angle = int(input(prompt))
            if angle <= 0:
                raise ValueError("Angle must be a positive integer.")
            return angle
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

while True:
    # Take inputs from the user
    print("Please enter the angles of the triangle:")
    angle1 = get_valid_angle("Enter the first angle: ")
    angle2 = get_valid_angle("Enter the second angle: ")
    angle3 = get_valid_angle("Enter the third angle: ")

    # Classify and print the type of triangle
    triangle_description = classify_triangle(angle1, angle2, angle3)
    print(f"The triangle is {triangle_description}.")

    # Ask the user if they want to classify another triangle or exit
    choice = input("Press 'e' to exit or any other key to classify another triangle: ").strip().lower()
    if choice == 'e':
        break