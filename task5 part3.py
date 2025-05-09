print("Hello, file 3")
def divide_two_numbers(a, b):
    if b == 0:
        return "Error: Cant divided by 0."
    return a / b

if __name__ == "__main__":
    result = divide_two_numbers(10, 2) 
    print(f"divide: {result}")
