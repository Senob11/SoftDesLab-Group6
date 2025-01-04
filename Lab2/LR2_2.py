def navigate_file():

    filename = input("Enter the filename: ")
    
    try:

        with open(filename, 'r') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip() != '']

        print(f"\nThe file has {len(lines)} non-empty lines.")

        while True:
            try:
                line_number = int(input("Enter a line number (0 to quit): "))
                
                if line_number == 0:
                    print("Exiting the program. Goodbye!")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1]}")
                else:
                    print("Error: The line number exceeds the total number of lines.")
            except ValueError:
                print("Error: Please enter a valid integer.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

navigate_file()
