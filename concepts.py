

import re
import time


# 1. ITERATOR

class CountUp:
    """Counts from 'start' up to 'stop' one step at a time."""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self                      # the object itself is the iterator

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration          # signals "no more items"
        value = self.current
        self.current += 1
        return value


print("=" * 50)
print("1. ITERATOR – CountUp(1, 5)")
print("=" * 50)
for num in CountUp(1, 5):
    print(num, end="  ")
print("\n")


# 2. GENERATOR

def even_numbers(limit):
    """Yields even numbers from 0 up to limit."""
    for n in range(0, limit + 1, 2):
        yield n                          # pauses here and returns n


print("=" * 50)
print("2. GENERATOR – even_numbers(10)")
print("=" * 50)
for even in even_numbers(10):
    print(even, end="  ")
print("\n")


# 3. DECORATOR

def timer(func):
    """Decorator: prints how long 'func' took to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  ⏱  '{func.__name__}' ran in {end - start:.4f} seconds")
        return result
    return wrapper


@timer                                   # same as: greet = timer(greet)
def greet(name):
    time.sleep(0.1)                      # simulate some work
    print(f"  Hello, {name}!")


print("=" * 50)
print("3. DECORATOR – @timer on greet()")
print("=" * 50)
greet("Alice")
print()


# 4. CLOSURE

def make_multiplier(factor):
    """Returns a function that multiplies any number by 'factor'."""
    def multiply(number):
        return number * factor           # 'factor' is remembered (closed over)
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("=" * 50)
print("4. CLOSURE – make_multiplier()")
print("=" * 50)
print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")
print()


# 5. REGULAR EXPRESSION (re)

text = "Contact us at support@example.com or sales@company.org for help."

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails_found = re.findall(email_pattern, text)

print("=" * 50)
print("5. REGULAR EXPRESSION – find emails")
print("=" * 50)
print(f"  Text   : {text}")
print(f"  Emails : {emails_found}")
print()

print("=" * 50)
print("All 5 concepts demonstrated successfully!")
print("=" * 50)