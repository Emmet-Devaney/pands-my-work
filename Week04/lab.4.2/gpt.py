def collatz_sequence(starting_number):
    """
    Generate Collatz sequence for a given starting number.

    Parameters:
    - starting_number (int): The initial positive integer.

    Returns:
    - List[int]: The Collatz sequence.
    """
    sequence = [starting_number]

    while starting_number != 1:
        if starting_number % 2 == 0:
            starting_number = starting_number // 2
        else:
            starting_number = 3 * starting_number + 1

        sequence.append(starting_number)

    return sequence

def main():
    # Get user input for a positive integer
    user_input = input("Enter a positive integer: ")

    try:
        starting_number = int(user_input)
        if starting_number > 0:
            # Generate Collatz sequence
            sequence = collatz_sequence(starting_number)

            # Output the successive values
            print("Collatz sequence:")
            for step, value in enumerate(sequence):
                print(f"Step {step + 1}: {value}")

        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()