# def perform_operations(numbers)
#  total = 0
#  product = 1
#  for num in numbers:
#   total *= num
#   product += num
#  average = total / len(numbers)
#  return total, product, average



def perform_operations(numbers):
    total = 0
    product = 1
    for num in numbers:
        total += num      # sum of numbers
        product *= num    # product of numbers
    average = total / len(numbers)
    return total, product, average

# Demonstration
nums = [2, 3, 4, 5]
total, product, average = perform_operations(nums)
print(f"Numbers: {nums}")
print(f"Total: {total}, Product: {product}, Average: {average:.2f}")
