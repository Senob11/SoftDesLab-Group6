# stats.py

def mean(numbers):
#function to get the average of a set of numbers
    return sum(numbers) / len(numbers)

def median(numbers):
#function to get the median of a set of numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2

    if n % 2 == 0:
        # Even number of elements: return the average of the middle two
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    else:
        # Odd number of elements: return the middle element
        return sorted_numbers[midpoint]

def mode(numbers):
#function to get the mode of a set of numbers
    frequency = {} #initializes frequency
    for number in numbers: 
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_frequency]

    return modes
    
#testing the functions
x = [1,5,8,6,3,5,4,7,8,6,2,1,4,5,6,3,2,5,8,9,7,6,5,4,1,3,6]

print(mean(x))
print(median(x))
print(mode(x)) 
