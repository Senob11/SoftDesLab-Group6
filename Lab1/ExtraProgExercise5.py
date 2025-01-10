# pi_iteration

def approximate_pi(iterations):
	approximation = 0
	for i in range(iterations):
		term = (-1) ** i / (2 * i + 1)
		approximation += term
	return approximation * 4

if __name__ == "__main__":
	print("Leibniz Calculator")
	try:
		iterations = int(input("Enter the number of iterations: "))
		if iterations <= 0:
			print("Invalid input. Please ensure the number of iterations is a positive integer.")
		else:
			pi_approximation = approximate_pi(iterations)
			print(f"The approximated value of pi after {iterations} iterations is: {pi_approximation:.10f}")
	except ValueError:
		print("Invalid input. Please enter a positive integer.")

