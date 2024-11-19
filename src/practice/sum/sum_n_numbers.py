from data.dataset import numbers
def sum_n_numbers(numbers, n):
    return n*(n+1)//2

def sum_n_numbers_2(numbers,n):
    return sum(numbers[:n]) # This ensures you’re summing only the first n elements of the list, no matter the list’s length.

print(sum_n_numbers(numbers,10))
print(sum_n_numbers_2(numbers,10))

