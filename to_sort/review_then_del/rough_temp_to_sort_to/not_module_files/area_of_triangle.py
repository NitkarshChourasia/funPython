def calculate_triangle_area(side1=3, side2=4, side3=5):
    if (
        isinstance(side1, (int, float))
        and isinstance(side2, (int, float))
        and isinstance(side3, (int, float))
    ):
        s = (side1 + side2 + side3) / 2  # What is S?
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5  # Heroin's Formula
        return area

    else:
        return "Only numbers are allowed."


def calculate_triangle_area(side1=3, side2=4, side3=5):
    if (
        isinstance(side1, (int, float))
        and isinstance(side2, (int, float))
        and isinstance(side3, (int, float))
    ):
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        return area
    else:
        return "Only numbers are allowed."


if __name__ == "__main__":
    test_cases = [
        # Extreme Test Cases
        (-2, 3, 4),
        (5, -5, 10),
        (10**9, 10**9, 10**9),
        # Edge Cases
        (0, 4, 5),
        (3, 0, 6),
        (5, 5, 5),  # Equilateral Triangle
        (3, 4, 5),  # Right-Angled Triangle
    ]

    for i, test_case in enumerate(test_cases):
        side1, side2, side3 = test_case
        result = calculate_triangle_area(side1, side2, side3)
        if isinstance(result, str):
            print(f"Test case {i+1}: {result}")
        else:
            print(f"Test case {i+1}: Area = {result:.2f}")


def calculate_triangle_area(side1=None, side2=None, side3=None):
    if side1 is None:
        side1 = float(input("Enter the first side length: "))
    if side2 is None:
        side2 = float(input("Enter the second side length: "))
    if side3 is None:
        side3 = float(input("Enter the third side length: "))

    if (
        isinstance(side1, (int, float))
        and isinstance(side2, (int, float))
        and isinstance(side3, (int, float))
    ):
        if side1 > 0 and side2 > 0 and side3 > 0:
            if (
                side1 + side2 > side3
                and side1 + side3 > side2
                and side2 + side3 > side1
            ):
                s = (side1 + side2 + side3) / 2
                area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
                return area
            else:
                return "The given side lengths do not form a valid triangle."
        else:
            return "Side lengths should be positive numbers."
    else:
        return "Only numbers are allowed."


if __name__ == "__main__":
    area = calculate_triangle_area()
    if isinstance(area, str):
        print(area)
    else:
        print(f"The area of the triangle is {area:.2f}")


# How and Can I use class, somehow to make the function run.
# Make it, clean.
