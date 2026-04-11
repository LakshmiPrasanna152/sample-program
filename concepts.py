

import re
import time



# 1. ITERATOR

class CountUp:
    """Counts from 'start' up to 'limit' one step at a time."""

    def __init__(self, start, limit):
        self.current = start
        self.limit = limit

    def __iter__(self):
        return self                     # the object itself is the iterator

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration         # signal: nothing left to iterate
        value = self.current
        self.current += 1
        return value



# 2. GENERATOR

def even_numbers(limit):
    """Yields even numbers from 0 up to limit."""
    for num in range(0, limit + 1, 2):
        yield num                       # pauses here and resumes on next()



# 3. DECORATOR
#  
def timer(func):
    """Decorator: prints how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  [timer] '{func.__name__}' ran in {end - start:.4f} seconds")
        return result
    return wrapper


@timer                                  # same as: greet = timer(greet)
def greet(name):
    """A simple greeter (decorated with @timer)."""
    message = f"Hello, {name}! Welcome to Python."
    print(f"  >> {message}")
    return message



# 4. CLOSURE

def make_multiplier(factor):
    """Returns a function that multiplies any number by 'factor'."""
    def multiply(number):               # 'factor' is captured in closure
        return number * factor
    return multiply                     # returns the inner function



# 5. REGULAR EXPRESSIONS (regex)

def validate_and_extract(text):
    """
    Uses regex to:
      - validate an email address
      - extract all phone numbers
      - find all hashtags
    """
    # Email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    email = "user.name@example.com"
    is_valid = bool(re.match(email_pattern, email))
    print(f"  Email '{email}' -> {'VALID' if is_valid else 'INVALID'}")

    # Extract phone numbers
    phone_pattern = r'\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b'
    phones = re.findall(phone_pattern, text)
    print(f"  Phone numbers found : {phones}")

    # Extract hashtags
    hashtag_pattern = r'#\w+'
    hashtags = re.findall(hashtag_pattern, text)
    print(f"  Hashtags found      : {hashtags}")


#  MAIN — run all five concepts

if __name__ == "__main__":

    # 1. Iterator
    print("=" * 50)
    print("1. ITERATOR  —  CountUp(1, 5)")
    print("=" * 50)
    counter = CountUp(1, 5)
    for num in counter:
        print(f"  {num}", end=" ")
    print()

    # 2. Generator
    print("\n" + "=" * 50)
    print("2. GENERATOR  —  even_numbers(10)")
    print("=" * 50)
    for even in even_numbers(10):
        print(f"  {even}", end=" ")
    print()

    # 3. Decorator
    print("\n" + "=" * 50)
    print("3. DECORATOR  —  @timer on greet()")
    print("=" * 50)
    greet("Alice")

    # 4. Closure
    print("\n" + "=" * 50)
    print("4. CLOSURE  —  make_multiplier()")
    print("=" * 50)
    double = make_multiplier(2)         # 'factor' = 2 is remembered
    triple = make_multiplier(3)         # 'factor' = 3 is remembered
    print(f"  double(6) = {double(6)}")
    print(f"  triple(6) = {triple(6)}")

    # 5. Regular Expressions
    print("\n" + "=" * 50)
    print("5. REGULAR EXPRESSIONS")
    print("=" * 50)
    sample_text = (
        "Call me at 123-456-7890 or 987.654.3210. "
        "#Python #coding is fun! "
        "Office: 555 123 4567"
    )
    print(f"  Text: {sample_text}")
    validate_and_extract(sample_text)

    print("\n" + "=" * 50)
    print("All 5 concepts demonstrated successfully!")
    print("=" * 50)