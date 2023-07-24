def count_ones_in_binary(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count
def custorm_sort(numbers):
    n =len(numbers)

    for i in range(n):
        for j in range(0, n-i-1):
            count_current= count_ones_in_binary(numbers[j])
            count_next= count_ones_in_binary(numbers[j+1])
            if count_current > count_next or (count_current==count_next and numbers[j] >numbers[j+1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

# Example usage:
numbers = [3, 7, 8, 9]
sorted_numbers = custorm_sort(numbers)
print(sorted_numbers)