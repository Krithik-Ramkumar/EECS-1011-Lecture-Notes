"""
EECS 1011 — Introduction to Variables, Types, and Expressions
=============================================================

This file is a first guided tour of three ideas that appear in almost every
program:

    * variables give names to values;
    * types describe what kind of values those are; and
    * expressions combine values to calculate a result.

Run the file from top to bottom. The print statements show the results of the
examples. You can also change the example values and run the file again.

Python version: Python 3
"""


# ---------------------------------------------------------------------------
# 1. Values and variables
# ---------------------------------------------------------------------------

# A value is a piece of data. Here, 17 is an integer value and "Ada" is a
# string value (text). A variable is a name that refers to a value.
student_name = "Ada"
credits_completed = 17

print("Student:", student_name)
print("Credits completed:", credits_completed)

# The = sign is the assignment operator. Read the line below as:
# "Calculate 18 + 1, then assign the result to credits_completed."
# Assignment does not mean that the two sides are mathematically equal.
credits_completed = credits_completed + 1
print("Credits after completing one more:", credits_completed)

# The shorter augmented-assignment form performs the same update:
credits_completed += 1  # Same idea as: credits_completed = credits_completed + 1
print("Credits after another update:", credits_completed)

# A variable can be assigned a new value later. Python is dynamically typed:
# a variable name is not permanently restricted to one type. Still, changing
# a variable from (for example) a number to unrelated text can make programs
# confusing, so choose a clear and consistent meaning for each variable.
example_value = 42
print("The value before reassignment:", example_value)
example_value = "Now this name refers to text"
print("A reassigned variable:", example_value)


# ---------------------------------------------------------------------------
# 2. Choosing and using variable names
# ---------------------------------------------------------------------------

# A Python identifier (a name for a variable, function, and so on) may contain
# letters, digits, and underscores, but it cannot start with a digit. Names
# are case-sensitive: score, Score, and SCORE are three different names.
course_code = "EECS 1011"
quiz_score = 8
quiz_score_max = 10

# Use descriptive names. A reader should be able to make a good guess about
# what a value represents without tracing the whole program.
print(course_code, "quiz:", quiz_score, "out of", quiz_score_max)

# By convention, Python variables use lowercase words separated by
# underscores (snake_case): temperature_c, item_count, and average_score.
# Avoid Python keywords such as if, for, class, and True as variable names.
# Also avoid names that shadow useful built-ins, such as list, str, or sum.

# These are examples of invalid names; they are intentionally kept inside
# comments so that this lesson remains runnable:
# 2nd_place = "not allowed"  # A variable name cannot start with a digit.
# student-name = "not allowed"  # A hyphen is treated as subtraction.
# class = "not allowed"  # "class" is a reserved Python keyword.


# ---------------------------------------------------------------------------
# 3. The basic built-in types
# ---------------------------------------------------------------------------

# int: whole numbers, positive, negative, or zero.
number_of_books = 3
temperature_change = -4

# float: numbers that can have a fractional part. A decimal point makes a
# number a float, even if the digits after the point are zero.
height_metres = 1.68
whole_looking_float = 5.0

# str: text. String literals are written between matching single or double
# quotes. Use triple quotes for text that spans multiple lines.
greeting = "Hello!"
message = 'Python accepts single quotes too.'
two_line_note = """This text
continues on a second line."""

# bool: a truth value. The only Boolean values are True and False (capitalized).
is_enrolled = True
has_submitted_lab = False

# None: a special value meaning "no value" or "not set." None is not the same
# thing as 0, False, or the string "None".
optional_middle_name = None

# type(value) reports the type of a value. It is especially useful when
# investigating a surprising result.
print("Type of number_of_books:", type(number_of_books).__name__)
print("Type of height_metres:", type(height_metres).__name__)
print("Type of greeting:", type(greeting).__name__)
print("Type of is_enrolled:", type(is_enrolled).__name__)
print("Type of optional_middle_name:", type(optional_middle_name).__name__)

# int and float are both numeric types. When an expression combines them,
# Python usually converts the integer to a float so the result can represent
# a fractional value.
combined_measurement = 2 + 0.5
print("2 + 0.5 =", combined_measurement)
print("Type of that result:", type(combined_measurement).__name__)


# ---------------------------------------------------------------------------
# 4. Arithmetic expressions
# ---------------------------------------------------------------------------

# An expression is code that Python evaluates to produce a value. The values
# and operators below form arithmetic expressions.
first_number = 14
second_number = 4

print("Addition:", first_number + second_number)          # 18
print("Subtraction:", first_number - second_number)       # 10
print("Multiplication:", first_number * second_number)    # 56
print("Division:", first_number / second_number)          # 3.5

# Integer division (//) rounds the quotient down to the nearest whole number.
# With positive values this looks like dropping the fractional part; with
# negative values it rounds down, not toward zero.
print("Floor division:", first_number // second_number)   # 3
print("Negative floor division:", -14 // 4)               # -4

# Modulo (%) gives the remainder after floor division. It is often useful for
# checking whether a number is divisible by another number.
print("Remainder:", first_number % second_number)          # 2
print("Is 14 even?", first_number % 2 == 0)               # False
print("Is 14 divisible by 7?", first_number % 7 == 0)     # True

# Exponentiation (**) raises a number to a power.
print("2 to the power of 5:", 2**5)                       # 32

# Parentheses make the intended order clear. In Python, exponentiation is
# evaluated before multiplication and division, which are before addition
# and subtraction. Parentheses can override that normal precedence.
print("Without parentheses:", 2 + 3 * 4)                  # 14
print("With parentheses:", (2 + 3) * 4)                   # 20
print("A more involved expression:", (10 - 2) / 4 + 3)    # 5.0

# Division by zero is undefined and raises ZeroDivisionError:
# invalid_result = 10 / 0  # Uncommenting this line stops the program.


# ---------------------------------------------------------------------------
# 5. Text expressions and formatted output
# ---------------------------------------------------------------------------

# The + operator joins (concatenates) strings. It does not automatically
# convert numbers to text.
first_name = "Grace"
last_name = "Hopper"
full_name = first_name + " " + last_name
print("Joined strings:", full_name)

# Repeating a string with * repeats its contents.
print("Ha" * 3)  # HaHaHa

# This raises TypeError because the operands have incompatible types:
# message = "Age: " + 20

# Convert a number to text with str() if concatenation is appropriate.
age = 20
print("Concatenation after conversion:", "Age: " + str(age))

# For messages containing values, f-strings are usually clearer. Put an f
# before the opening quote and place expressions inside curly braces.
course_average = 84.275
print(f"{full_name} is {age} years old.")
print(f"The course average is {course_average:.1f}%.")  # Display one decimal.

# The formatting above changes how a number is displayed; it does not change
# the value stored in course_average.
print("The stored average is still:", course_average)


# ---------------------------------------------------------------------------
# 6. Comparisons produce Boolean values
# ---------------------------------------------------------------------------

# Comparison operators compare values. Each comparison expression evaluates
# to either True or False.
score = 76
passing_score = 50

print("score == 76:", score == 76)  # Equal to
print("score != 50:", score != 50)  # Not equal to
print("score > 50:", score > passing_score)
print("score >= 76:", score >= 76)
print("score < 100:", score < 100)
print("score <= 75:", score <= 75)

# Do not confuse = (assignment) with == (comparison):
# score = 76    assigns 76 to score
# score == 76   asks whether score equals 76 and gives True or False

# Strings can be compared too. Equality checks whether their contents match.
print("Does the course code match?", course_code == "EECS 1011")


# ---------------------------------------------------------------------------
# 7. Combining conditions with Boolean operators
# ---------------------------------------------------------------------------

# and is True only when both conditions are True.
# or is True when at least one condition is True.
# not reverses a Boolean value.
has_id = True
is_old_enough = True
has_guest_pass = False

can_enter_alone = has_id and is_old_enough
can_enter_with_permission = can_enter_alone or has_guest_pass

print("Can enter alone?", can_enter_alone)
print("Can enter with permission?", can_enter_with_permission)
print("Does not have an ID?", not has_id)

# Comparisons can be joined into a range check. The chained expression
# 0 <= score <= 100 means (0 <= score) and (score <= 100).
score_is_valid = 0 <= score <= 100
print("Is the score between 0 and 100?", score_is_valid)

# Prefer explicit parentheses when combining several different conditions:
eligible_for_award = (score >= 90 and has_submitted_lab) or has_guest_pass
print("Eligible for the example award?", eligible_for_award)


# ---------------------------------------------------------------------------
# 8. Converting between types
# ---------------------------------------------------------------------------

# Conversion functions can construct values of a different type:
numeric_text = "125"
converted_integer = int(numeric_text)
converted_decimal = float("3.75")
converted_text = str(125)

print("Converted text to integer:", converted_integer)
print("Converted text to float:", converted_decimal)
print("Converted integer to text:", converted_text)

# A conversion only works when the input makes sense for the target type.
# int("hello") raises ValueError, and int("3.75") also raises ValueError.
# Convert decimal text to float first if a decimal is expected:
decimal_text = "3.75"
decimal_value = float(decimal_text)
print("Decimal text as a number:", decimal_value)

# Converting a float to int discards the fractional part (it does not round):
print("int(4.9):", int(4.9))  # 4

# bool() follows Python's truth-value rules. In particular, zero and empty
# strings are False, while non-empty strings (including "False") are True.
print("bool(0):", bool(0))
print("bool(5):", bool(5))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))


# ---------------------------------------------------------------------------
# 9. Input and the type of input()
# ---------------------------------------------------------------------------

# input(prompt) displays a prompt and returns what the user typed as a string.
# Uncomment the next two lines to try interactive input:
#
# typed_text = input("Enter a whole number: ")
# typed_number = int(typed_text)
# print("One more than your number is", typed_number + 1)
#
# The conversion is necessary: without int(), typed_text + "1" would join two
# strings instead of performing numeric addition. If the user types something
# that is not a whole number, int() raises ValueError.


# ---------------------------------------------------------------------------
# 10. Expressions in context: calculating a rectangle
# ---------------------------------------------------------------------------

# A useful way to learn expressions is to turn a small problem into named
# quantities and a formula. This example calculates a rectangle's area and
# perimeter. The units are metres and square metres.
rectangle_length_m = 8.0
rectangle_width_m = 3.5

rectangle_area_m2 = rectangle_length_m * rectangle_width_m
rectangle_perimeter_m = 2 * (rectangle_length_m + rectangle_width_m)

print(f"Rectangle area: {rectangle_area_m2:.2f} m^2")
print(f"Rectangle perimeter: {rectangle_perimeter_m:.2f} m")

# If either dimension is negative, the measurements are probably invalid.
# This Boolean expression checks the assumptions before using the values.
dimensions_are_valid = rectangle_length_m > 0 and rectangle_width_m > 0
print("Are both dimensions positive?", dimensions_are_valid)


# ---------------------------------------------------------------------------
# 11. Common beginner mistakes
# ---------------------------------------------------------------------------

# 1) Using a name before assigning it causes NameError:
# print(unassigned_value)

# 2) Mixing text and numbers with + causes TypeError unless you convert:
# print("There are " + 3 + " students")
# Better: use an f-string.
student_count = 3
print(f"There are {student_count} students")

# 3) Misspelling a variable name creates a different name:
assignment_total = 5
# print(assignments_total)  # NameError: this spelling was never assigned.
print("Assignments:", assignment_total)

# 4) Integer division is not ordinary division:
print("7 / 2 =", 7 / 2)    # 3.5
print("7 // 2 =", 7 // 2)  # 3

# 5) Floating-point values are approximations in binary. Some decimal
# fractions cannot be represented exactly, so avoid relying on exact equality
# for calculations that involve floats.
print("0.1 + 0.2 is exactly 0.3?", 0.1 + 0.2 == 0.3)
# For more precise comparisons, the math module provides isclose():
import math

print("Are they close?", math.isclose(0.1 + 0.2, 0.3))


# ---------------------------------------------------------------------------
# 12. Practice: predict, then check
# ---------------------------------------------------------------------------

# Before running these statements, try to predict each result. Then run the
# file and compare your predictions with the printed answers.
practice_a = 9 + 2 * 3
practice_b = (9 + 2) * 3
practice_c = 17 // 5
practice_d = 17 % 5
practice_e = "ha" * 2
practice_f = 4 < 7 and 10 == 10

print("Practice A (9 + 2 * 3):", practice_a)
print("Practice B ((9 + 2) * 3):", practice_b)
print("Practice C (17 // 5):", practice_c)
print("Practice D (17 % 5):", practice_d)
print('Practice E ("ha" * 2):', practice_e)
print("Practice F (4 < 7 and 10 == 10):", practice_f)

# Try these extensions:
#   * Change the rectangle dimensions and recalculate its area and perimeter.
#   * Store your own name and number of courses in variables, then print them
#     with an f-string.
#   * Convert a string containing a decimal number to float and multiply it.
#   * Write a Boolean expression that checks whether a number is negative OR
#     greater than 100.


# ---------------------------------------------------------------------------
# Key ideas to remember
# ---------------------------------------------------------------------------

# * A variable is a descriptive name associated with a value.
# * A value has a type, such as int, float, str, bool, or NoneType.
# * An expression combines values, names, and operators to produce a value.
# * Assignment (=) stores a value; equality (==) compares two values.
# * Parentheses make grouping explicit and help expressions stay readable.
# * Convert input text to a numeric type before doing numeric calculations.
# * Clear names and short, well-commented expressions make programs easier to
#   understand, test, and change.