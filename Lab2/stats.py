def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[mid]
    return (numbers[mid] + numbers[mid - 1]) / 2

def mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    for key, value in freq.items():
        if value == max_freq:
            return key

def main():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(num) for num in user_input.split()]
        if not numbers:
            print("No numbers provided. Exiting program.")
            return
        print(f"Numbers: {numbers}")
        print(f"Mean: {mean(numbers)}")
        print(f"Median: {median(numbers)}")
        print(f"Mode: {mode(numbers)}")
    except ValueError:
        print("Error: Please enter valid numbers.")

main()

