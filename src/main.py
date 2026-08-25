from utils import square, is_even, celsius_to_fahrenheit, greet

def process_number(n):
    print(f"Number: {n}")
    print(f"Square: {square(n)}")
    print(f"Is Even: {is_even(n)}")
    print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(n)}")
    print("-" * 20)

if __name__ == "__main__":
    print(greet("User"))
    for _ in range(3):
        val = float(input("Enter a number: "))
        process_number(val)
