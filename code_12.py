def get_fibonacci_number(position):
    
    if position == 1:
        return 1
    elif position == 2:
        return 1
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)

def get_fibonacci_number_sequence(number):
    stored_numbers = []
    for i in range(1, number + 1):
        stored_numbers.append(get_fibonacci_number(i))
    return stored_numbers

if __name__ == "__main__":
    # Example output for Fibonacci number at a specific position
    print(get_fibonacci_number(6))  # Should output 8
    # Example output for Fibonacci sequence up to a specified number of elements
    print(get_fibonacci_number_sequence(9))  # Should output [1, 1, 2, 3, 5, 8, 13, 21, 34]