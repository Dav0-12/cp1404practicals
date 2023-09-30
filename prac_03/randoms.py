"""Prac 3 Randoms - Questions Answers"""
import random

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# We saw random integers between 5 and 20 inclusive. The smallest number
# is 5 and the largest number is 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# We saw a random integer between 3 and 10, incrementing by 2. Therefore, the only possible
# random numbers from this function are 3, 5, 7, 9. A 4 therefore could not be produced.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# We saw a random float between 2.5 and 5.5 inclusive. The smallest number
# is therefore 2.5 and the largest number is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
