def calculate_total_distance(initial_height, bounciness_index, num_bounces):
    """
    Calculate the total distance traveled by a ball after a given number of bounces.
    """
    total_distance = 0
    current_height = initial_height

    for _ in range(num_bounces):
        # Ball falls down
        total_distance += current_height
        # Ball bounces back up
        current_height *= bounciness_index
        total_distance += current_height

    return total_distance

# Main program
if __name__ == "__main__":
    print("Bouncing Ball Distance Calculator")

    try:
        initial_height = float(input("Enter the initial height of the ball (in feet): "))
        bounciness_index = float(input("Enter the bounciness index (a value between 0 and 1): "))
        num_bounces = int(input("Enter the number of bounces: "))

        # Validate inputs
        if initial_height <= 0 or bounciness_index <= 0 or bounciness_index >= 1 or num_bounces < 0:
            print("Invalid input. Please ensure the height is positive, the bounciness index is between 0 and 1, and the number of bounces is non-negative.")
        else:
            total_distance = calculate_total_distance(initial_height, bounciness_index, num_bounces)
            print(f"The total distance traveled by the ball is: {total_distance:.2f} feet.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
