from utils import square, is_even, celsius_to_fahrenheit

def process_number(n):
    print(f"--- Results for {n} ---")
    print(f"Square: {square(n)}")
    print(f"Is Even: {is_even(n)}")
    print(f"As Celsius to Fahrenheit: {celsius_to_fahrenheit(n):.2f}°F\n")

if __name__ == "__main__":
    for _ in range(3):
        val = float(input("Enter a number: "))
        process_number(val)# Final PR change
