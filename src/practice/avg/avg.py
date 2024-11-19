from numpy import mean
from data.dataset import numbers

def calc_avg_lib(numbers):
    return mean(numbers)

def calc_avg_pure(number):
    return sum(numbers)/len(numbers)

print(calc_avg_lib(numbers))
print(calc_avg_pure(numbers))