# Write a function that computes the digit sum of an integer. For example, digit_sum(142857) should return 27 (= 1 + 4 + 2 + 8 + 5 + 7).

# Proceed as follows:

# Convert the integer parameter into a string and then a list of digits.
# Loop over this list, converting each digit to an int and adding it to a running total.
# Return that running total.
# What is the digit sum of 3^{99} ?

def digit_sum(n):
    digits = list(str(n)) # list of stringified digits
    total = 0 # initialize the digit sum
    for i in range(len(digits)):
        # convert each entry to an int and add it to the sum
        total = total + int(digits[i])
    return total

print(digit_sum(3**99))
print(digit_sum(3**1))
print(digit_sum(3**100))