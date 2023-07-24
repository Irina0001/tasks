def max_multiplication(input_string):
    if not isinstance(input_string, str):
        return None

    max_product = None
    for i in range(len(input_string)-3):
        current_sequence = input_string[i:i+4]
        if current_sequence.isdigit():
            product = 1
            for digit in current_sequence:
                product*= int(digit)
            if max_product is None or product > max_product:
                max_product = product

    return max_product
# Example:
result1 = max_multiplication ('abc 123456 def')
print(result1)

result2 = max_multiplication('a1b2c3d4e')
print(result2)
