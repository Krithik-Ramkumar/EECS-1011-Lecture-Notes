"""
EECS 1011 — Loops and Iteration
==============================

Loops repeat a block of code. They are useful when a task needs to be done
multiple times, such as processing every value in a collection or repeating
an action until a condition changes.

This lesson introduces:

    * for loops and iterables;
    * range() and counting loops;
    * while loops and loop conditions;
    * accumulators and running totals;
    * break, continue, and loop else;
    * nested loops, enumerate(), and common loop patterns; and
    * off-by-one errors, infinite loops, and other common mistakes.

Run this file from top to bottom. The examples use fixed data and do not
require user input. The interactive examples near the end are commented out.

Python version: Python 3
"""


# ---------------------------------------------------------------------------
# 1. What is a loop?
# ---------------------------------------------------------------------------

# A loop runs a block of code repeatedly. Without a loop, repeating the same
# instruction would require writing it over and over:
print("Good morning!")
print("Good morning!")
print("Good morning!")

# A loop expresses that repetition once. The indented body runs once for each
# item in the sequence:
for repetition_number in range(3):
    print("Good morning!")

# repetition_number is assigned each value from range(3), in turn: 0, 1, 2.
# The loop body therefore runs three times. The variable only has meaning as
# the loop progresses; after the loop it retains its final value in Python.


# ---------------------------------------------------------------------------
# 2. for loops: process each item in an iterable
# ---------------------------------------------------------------------------

# A for loop visits items from an iterable, one at a time. An iterable is an
# object that can provide its items in sequence, such as a string, list, or
# range.
course_code = "EECS 1011"

for character in course_code:
    print("Character:", character)

# Each pass through the loop is called an iteration. On each iteration,
# character refers to the next character in course_code. Spaces are characters
# too, so this string has a space as one of its iterated values.

student_names = ["Ari", "Bea", "Chen"]

for name in student_names:
    print("Welcome,", name)

# The loop variable name is a normal variable name; choose one that explains
# what each item represents. The plural collection / singular item convention
# is often helpful: for student in students.


# ---------------------------------------------------------------------------
# 3. Counting with range()
# ---------------------------------------------------------------------------

# range(stop) produces integers starting at 0 and ending just before stop.
# Therefore range(5) represents 0, 1, 2, 3, 4: five numbers, not six.
for number in range(5):
    print("Count from zero:", number)

# range(start, stop) starts at start and still stops before stop.
for number in range(2, 6):
    print("Count from two:", number)  # 2, 3, 4, 5

# range(start, stop, step) adds step each time. The stop value is still
# excluded. A negative step counts downward.
for number in range(0, 10, 2):
    print("Even number:", number)  # 0, 2, 4, 6, 8

for number in range(5, 0, -1):
    print("Countdown:", number)  # 5, 4, 3, 2, 1

# range() needs an integer step. A step of zero is invalid, and a step in the
# wrong direction may produce no values. For example, range(1, 5, -1) is empty.

# To count from 1 through 5 (including 5), the stop value needs to be 6:
for number in range(1, 6):
    print("One-based count:", number)


# ---------------------------------------------------------------------------
# 4. while loops: repeat while a condition is true
# ---------------------------------------------------------------------------

# A while loop checks its Boolean condition before every iteration. If the
# condition is True, the body runs. Then the condition is checked again.
count = 1

while count <= 4:
    print("while count:", count)
    count += 1  # Update the condition's variable so the loop can eventually end.

# Trace the values:
#   * initially count is 1, so 1 <= 4 is True;
#   * each iteration prints count and increases it by 1;
#   * when count becomes 5, 5 <= 4 is False and the loop ends.

# A while loop is useful when the number of repetitions is not known in
# advance, such as repeating until a user chooses to quit or until a target is
# reached. A for loop is often simpler when processing a known sequence.


# ---------------------------------------------------------------------------
# 5. Avoiding infinite loops
# ---------------------------------------------------------------------------

# A while loop needs a path that makes its condition eventually False. If the
# condition stays True forever, the loop is infinite.
#
# This example is intentionally commented out; running it would not end:
#
# count = 1
# while count <= 4:
#     print(count)
#     # BUG: count never changes, so count <= 4 remains True.
#
# A good while-loop checklist:
#   1. What condition keeps the loop going?
#   2. Which statements can change values used by that condition?
#   3. Can every possible path eventually make the condition False?
#
# Avoid changing the loop condition in a way that accidentally prevents
# termination. For example, decrementing a counter that must reach a larger
# stopping value can make it run forever.


# ---------------------------------------------------------------------------
# 6. Accumulators: build a result as the loop runs
# ---------------------------------------------------------------------------

# An accumulator is a variable that collects a result across iterations.
# Initialize it before the loop, then update it during each iteration.
quiz_scores = [8, 10, 7, 9]
total_score = 0

for score in quiz_scores:
    total_score += score

print("Total quiz score:", total_score)

# Calculate an average by dividing the accumulated total by the number of
# values. Guard against an empty collection to avoid division by zero.
if len(quiz_scores) > 0:
    average_score = total_score / len(quiz_scores)
    print(f"Average quiz score: {average_score:.2f}")
else:
    print("There are no scores to average.")

# A counter is a related pattern: it records how many times an event occurs.
passing_count = 0

for score in quiz_scores:
    if score >= 8:
        passing_count += 1

print("Number of scores at least 8:", passing_count)

# Initialize accumulators with a suitable starting value:
#   * sum: usually 0;
#   * product: usually 1;
#   * count: usually 0;
#   * a result list: usually [].
#
# Starting a sum at 1 or a product at 0 would change the result.


# ---------------------------------------------------------------------------
# 7. Transforming and filtering values
# ---------------------------------------------------------------------------

# A loop can transform each input item and place the result in a new list.
celsius_values = [0, 10, 20, 30]
fahrenheit_values = []

for celsius in celsius_values:
    fahrenheit = celsius * 9 / 5 + 32
    fahrenheit_values.append(fahrenheit)

print("Celsius values:", celsius_values)
print("Fahrenheit values:", fahrenheit_values)

# A loop can also filter items: copy only the values that meet a condition.
all_numbers = [3, 8, 11, 14, 19, 22]
even_numbers = []

for value in all_numbers:
    if value % 2 == 0:
        even_numbers.append(value)

print("Even values:", even_numbers)

# append(value) adds one item to the end of a list. The list being built must
# be initialized before the loop. If you reset it inside the loop, earlier
# results will be discarded on each iteration.


# ---------------------------------------------------------------------------
# 8. Indexes and enumerate()
# ---------------------------------------------------------------------------

# Sometimes a program needs an item's position as well as its value. Python
# indexes start at 0, so the first item is at index 0.
colors = ["red", "green", "blue"]
print("First color:", colors[0])
print("Number of colors:", len(colors))

# A range of indexes can be formed with range(len(collection)), but enumerate()
# is usually clearer. It provides both an index and its corresponding item.
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# Give enumerate() a start value to count from 1 for display. This changes the
# reported index, not the actual list indexes.
for display_number, color in enumerate(colors, start=1):
    print(f"{display_number}. {color}")

# Use the value directly when you do not need the index. Indexing can be
# useful when changing an existing list item, but iterating over values is
# often simpler for reading or calculating.


# ---------------------------------------------------------------------------
# 9. break: leave a loop early
# ---------------------------------------------------------------------------

# break immediately exits the nearest enclosing loop. Here it ends the search
# as soon as the requested value is found.
target = 14
numbers_to_search = [5, 9, 14, 18, 22]
found = False

for value in numbers_to_search:
    if value == target:
        found = True
        print("Found the target:", value)
        break

if not found:
    print("The target was not found.")

# If a break is inside nested loops, it only exits the innermost loop that
# contains it. The outer loop continues unless it too is ended or controlled.


# ---------------------------------------------------------------------------
# 10. continue: skip to the next iteration
# ---------------------------------------------------------------------------

# continue skips the rest of the current iteration and proceeds to the next
# item. It does not end the entire loop.
for number in range(1, 8):
    if number % 2 == 0:
        continue  # Skip even numbers.
    print("Odd number:", number)

# Use continue only when it makes the loop easier to understand. Sometimes an
# if statement without continue is more straightforward:
for number in range(1, 8):
    if number % 2 != 0:
        print("Odd number, written with if:", number)

# In a while loop, make sure every path still updates the loop condition.
# A continue executed before that update can accidentally create an infinite
# loop. Example of a bug (kept commented out):
#
# count = 0
# while count < 5:
#     if count == 2:
#         continue  # BUG: count remains 2 forever.
#     count += 1


# ---------------------------------------------------------------------------
# 11. Loop else: completion without break
# ---------------------------------------------------------------------------

# A loop may have an else block. It runs when the loop finishes normally,
# including when a for loop has no items. It does NOT run if break exits the
# loop.
search_value = 7

for candidate in [2, 4, 6, 8]:
    if candidate == search_value:
        print("Found the value.")
        break
else:
    print("The loop completed without finding the value.")

# The else aligns with for (not with if). This pattern is useful for searches,
# but can surprise readers. A Boolean found flag, as in the previous section,
# may be clearer for beginners or when more logic is needed after the loop.


# ---------------------------------------------------------------------------
# 12. Nested loops
# ---------------------------------------------------------------------------

# A nested loop is a loop inside another loop. For every iteration of the
# outer loop, the inner loop completes all of its iterations.
for row in range(1, 4):
    for column in range(1, 5):
        print(f"({row}, {column})", end=" ")
    print()  # Move to a new output line after one row is complete.

# The inner loop above runs 4 times for each of 3 outer iterations, for
# 3 * 4 = 12 total coordinate pairs.

# Nested loops are useful for grids, tables, and comparing pairs of values.
# They can also be more expensive: if each of two loops handles n items, the
# body runs n * n times. Consider the amount of work when collections grow.


# ---------------------------------------------------------------------------
# 13. Choosing for or while
# ---------------------------------------------------------------------------

# Prefer for when you have a sequence or a known number of repetitions:
for attempt_number in range(1, 4):
    print("Attempt", attempt_number)

# Prefer while when repetition depends on a condition that changes:
fuel_remaining = 3
while fuel_remaining > 0:
    print("Using one unit of fuel.")
    fuel_remaining -= 1

# Both can solve many of the same problems. Choose the structure that makes
# the stopping rule and the work easiest to understand.


# ---------------------------------------------------------------------------
# 14. Common loop errors
# ---------------------------------------------------------------------------

# 1) Off-by-one errors: range(stop) excludes stop.
print("range(4) has values 0, 1, 2, 3:")
for value in range(4):
    print(value, end=" ")
print()

# To include 4 when counting from 0, use range(5). Always check whether the
# desired endpoints are inclusive and test the first and last values.

# 2) Updating the wrong variable:
#
# count = 0
# while count < 3:
#     other_variable += 1  # BUG: count never changes.
#
# 3) Resetting a running total in the loop:
#
# total = 0
# for value in [1, 2, 3]:
#     total = 0  # BUG: resets the result every iteration.
#     total += value
#
# Initialize total before the loop, then only update it inside.

# 4) Changing a collection while iterating over it can skip items or produce
# confusing behavior. Prefer creating a new result collection:
source_values = [1, 2, 3, 4, 5, 6]
remaining_values = []
for value in source_values:
    if value % 2 != 0:
        remaining_values.append(value)
print("Original values:", source_values)
print("Odd values in a new list:", remaining_values)

# 5) Using a loop when a built-in operation is clearer. For example, sum()
# already adds values in an iterable:
print("Built-in sum:", sum([2, 4, 6]))
# A hand-written loop is still valuable for learning and for custom logic.


# ---------------------------------------------------------------------------
# 15. Optional interactive loop: repeat until a sentinel value
# ---------------------------------------------------------------------------

# A sentinel is a special input value that signals "stop." This example
# continues asking for numbers until the user types "done". It uses input()
# and float(), so uncomment to run it interactively:
#
# running_total = 0.0
# entry_count = 0
# while True:
#     user_text = input("Enter a number, or 'done' to finish: ")
#     if user_text == "done":
#         break
#     number = float(user_text)
#     running_total += number
#     entry_count += 1
#
# if entry_count > 0:
#     print("Total:", running_total)
#     print("Average:", running_total / entry_count)
# else:
#     print("No numbers were entered.")
#
# This example uses break because the user determines when to stop. In a
# polished interactive program, invalid numeric input should also be handled
# appropriately rather than allowing float() to raise ValueError.


# ---------------------------------------------------------------------------
# 16. Practice: predict, then check
# ---------------------------------------------------------------------------

# Predict the output or final value before running each example.

# Practice A: How many times does the loop run, and what values are printed?
practice_a_values = []
for value in range(2, 8, 2):
    practice_a_values.append(value)
print("Practice A:", practice_a_values)

# Practice B: What is the final total?
practice_total = 0
for value in [3, 5, 7]:
    practice_total += value
print("Practice B total:", practice_total)

# Practice C: Which values are skipped?
practice_c_values = []
for value in range(6):
    if value == 3:
        continue
    practice_c_values.append(value)
print("Practice C:", practice_c_values)

# Practice D: Does the loop's else block run?
for value in [1, 3, 5]:
    if value == 4:
        break
else:
    print("Practice D: no break occurred")

# Try these extensions:
#   * Write a loop that prints the multiples of 5 from 5 through 50.
#   * Find the largest value in a list without using max().
#   * Count how many values in a list are negative, zero, and positive.
#   * Use a while loop to count down to zero, then print "Liftoff!"
#   * Create a small multiplication table using nested loops.
#   * For each exercise, identify its initialization, condition/sequence,
#     body, and update or next-item step.


# ---------------------------------------------------------------------------
# Key ideas to remember
# ---------------------------------------------------------------------------

# * A loop repeats a block of indented statements.
# * for visits each item in an iterable; range() is useful for counting.
# * while repeats as long as its condition is True.
# * A while loop needs a reliable way to reach a False condition.
# * Accumulators must be initialized before a loop and updated during it.
# * break exits the nearest loop; continue skips to the next iteration.
# * A loop's else runs only if the loop ends without break.
# * Nested loops multiply the number of iterations.
# * Check range endpoints and boundary values to avoid off-by-one errors.
# * Trace a loop one iteration at a time when its behavior is unclear.