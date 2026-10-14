"""
EECS 1011 — Branching and Conditionals
======================================

Programs normally execute one statement after another, from top to bottom.
Branching lets a program choose which statements to run based on a condition.
This is how a program can respond differently to different data.

This lesson introduces:

    * Boolean conditions and comparison operators;
    * if, elif, and else;
    * indentation and the structure of a decision;
    * combining conditions with and, or, and not;
    * nested decisions, guard clauses, and common logic errors; and
    * a compact conditional expression.

Run this file from top to bottom. The examples use fixed values so the whole
lesson runs without requiring interactive input. Later in the file, there are
commented input examples you can enable to experiment.

Python version: Python 3
"""


# ---------------------------------------------------------------------------
# 1. What is branching?
# ---------------------------------------------------------------------------

# A branch is a choice in the flow of a program. The condition is evaluated;
# if it is True, one block runs, and otherwise another path may be chosen.
# Conditions are expressions whose result is a Boolean: True or False.

temperature_c = 28

print("The program starts here.")

if temperature_c > 25:
    # This indented statement is the body of the if statement.
    print("It is a warm day.")

print("The program continues here, whether or not the branch ran.")

# With temperature_c set to 28, the condition 28 > 25 is True, so the indented
# print executes. Change temperature_c to 20 and run the file again: the
# condition is False and that print is skipped.


# ---------------------------------------------------------------------------
# 2. The basic if / else structure
# ---------------------------------------------------------------------------

# Use else when exactly one of two paths should run:
temperature_c = 18

if temperature_c >= 20:
    print("The temperature is at least 20 degrees.")
else:
    print("The temperature is below 20 degrees.")

# Python evaluates the condition once. Exactly one of these two blocks runs:
#   * the if block when its condition is True;
#   * the else block when its condition is False.
#
# else does not have its own condition. It means "in every remaining case."


# ---------------------------------------------------------------------------
# 3. Indentation defines a block
# ---------------------------------------------------------------------------

# Python uses indentation (leading spaces) to show which statements belong to
# a branch. The conventional style is four spaces per indentation level.
#
# In this example, both print calls belong to the if block. The final print is
# not indented, so it runs after the decision regardless of its result.
is_raining = True

if is_raining:
    print("Bring an umbrella.")
    print("A rain jacket may also be useful.")

print("Check the forecast again later.")

# Keep indentation consistent. Mixing tabs and spaces, or indenting a line
# incorrectly, can cause IndentationError or make the program's logic differ
# from what you intended.
#
# A colon (:) ends the if/else header and begins its indented block:
# if condition:
#     statements_to_run_when_true
# else:
#     statements_to_run_when_false


# ---------------------------------------------------------------------------
# 4. Conditions and comparison operators
# ---------------------------------------------------------------------------

# Comparisons usually make the conditions used by if statements. A comparison
# evaluates to True or False.
quiz_score = 82

print("Equal to 82:", quiz_score == 82)
print("Not equal to 0:", quiz_score != 0)
print("Greater than 50:", quiz_score > 50)
print("At least 80:", quiz_score >= 80)
print("Less than 100:", quiz_score < 100)
print("At most 100:", quiz_score <= 100)

# Use == to compare two values. A single = assigns a value to a variable.
# quiz_score = 82       # Assignment: store 82 in quiz_score.
# quiz_score == 82      # Comparison: ask whether it currently equals 82.

if quiz_score >= 50:
    print("The quiz score meets the example passing threshold.")

# Comparisons may be chained to check a range. This is equivalent to checking
# both comparisons with and:
score_is_in_range = 0 <= quiz_score <= 100
print("Is the score between 0 and 100?", score_is_in_range)

# A range check is only as good as its boundaries. Here both 0 and 100 count
# as valid. Use 0 < value < 100 if the endpoints should not count.


# ---------------------------------------------------------------------------
# 5. Choosing between several cases with elif
# ---------------------------------------------------------------------------

# elif means "else if." Python checks conditions from top to bottom. The body
# belonging to the first True condition runs, and the rest of the chain is
# skipped. If none is True, else runs (if it is present).
score = 86

if score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"A score of {score} receives grade {letter_grade}.")

# The order matters. A score of 86 is also greater than 70 and 60, but it
# matches score >= 80 first, so it receives "B." Later conditions are not
# checked after a match.
#
# A common bug is putting a broad condition first:
#
# if score >= 60:
#     letter_grade = "D"
# elif score >= 90:
#     letter_grade = "A"  # Unreachable: every score >= 90 matched the first if.
#
# Put the most specific/highest threshold first when using descending ranges.

# An else is optional. If no condition matches and there is no else, Python
# simply skips every block in the chain and continues after it.
wind_speed_kmh = 12
if wind_speed_kmh > 50:
    print("Strong wind warning.")

print("Wind check complete.")


# ---------------------------------------------------------------------------
# 6. Combining conditions: and, or, and not
# ---------------------------------------------------------------------------

# and requires every condition to be True.
# or requires at least one condition to be True.
# not reverses True and False.
has_student_id = True
is_registered = True
has_guest_pass = False

if has_student_id and is_registered:
    print("Access granted to the student lab.")
else:
    print("Student lab access denied.")

if has_guest_pass or is_registered:
    print("The person may enter the event.")

if not has_guest_pass:
    print("This person is not entering as a guest.")

# Parentheses make a multi-part condition easier to read. They also make the
# intended grouping explicit:
age = 19
has_permission = False

if age >= 18 and (has_student_id or has_permission):
    print("The age and identification/permission requirements are met.")

# Be careful with the meaning of English words such as "and" and "or." For
# example, "age is at least 18 and has ID or permission" can be ambiguous.
# Parentheses document which requirement must be combined with which choice.


# ---------------------------------------------------------------------------
# 7. Short-circuit evaluation
# ---------------------------------------------------------------------------

# Python evaluates Boolean expressions from left to right and may stop early:
#   * A and B: if A is False, B cannot make the whole expression True.
#   * A or B: if A is True, B cannot make the whole expression False.
# This is called short-circuit evaluation.
#
# It can be useful for safe checks. The second part below is evaluated only
# after the first part confirms that the list has at least one item.
scores = [78, 91, 84]

if len(scores) > 0 and scores[0] >= 50:
    print("There is a first score and it meets the threshold.")

# Reversing the parts would be unsafe for an empty list because scores[0]
# would be accessed before checking its length:
# if scores[0] >= 50 and len(scores) > 0:
#     print("This ordering can fail when scores is empty.")
#
# The same principle is often used when checking a value before using it.


# ---------------------------------------------------------------------------
# 8. Truthiness: conditions do not always need comparisons
# ---------------------------------------------------------------------------

# if can test a Boolean directly:
is_ready = True
if is_ready:
    print("Ready to begin.")

# Python also treats some non-Boolean values as true or false in conditions.
# Common false values include False, None, numeric zero, and empty containers
# or strings. Most other values are true. This behavior is called truthiness.
student_name = "Maya"
optional_note = ""

if student_name:
    print("A student name was provided:", student_name)

if not optional_note:
    print("There is no optional note.")

# Truthiness can be concise, but use an explicit comparison when the intended
# test is not simply "is this empty/nonzero?" For example:
number_of_attempts = 0
if number_of_attempts == 0:
    print("No attempts have been made.")

# Do not use a string containing "False" to mean the Boolean value False:
# bool("False") is True because it is a non-empty string. Use the Boolean
# literals True and False, or compare user input explicitly.


# ---------------------------------------------------------------------------
# 9. Nested conditionals
# ---------------------------------------------------------------------------

# An if statement can appear inside another if statement. This is called
# nesting. The inner decision is reached only if the outer condition is True.
account_is_active = True
password_is_correct = True
has_two_factor_code = False

if account_is_active:
    if password_is_correct:
        if has_two_factor_code:
            print("Sign-in successful.")
        else:
            print("Enter the two-factor code.")
    else:
        print("The password is incorrect.")
else:
    print("This account is inactive.")

# Nested conditions model sequential checks, but too much nesting is hard to
# read. Sometimes a combined condition communicates the rule more clearly:
if account_is_active and password_is_correct and has_two_factor_code:
    print("All sign-in requirements are satisfied.")

# Use nesting when the inner decision is meaningful only in the outer case;
# use a combined condition when it is simply a list of requirements. Do not
# change the logic just to make the code shorter.


# ---------------------------------------------------------------------------
# 10. Guard clauses and handling invalid data
# ---------------------------------------------------------------------------

# A guard clause checks an invalid or special case early. This makes it clear
# when the ordinary calculation is allowed to proceed.
denominator = 4

if denominator == 0:
    print("Cannot divide by zero.")
else:
    quotient = 20 / denominator
    print("Quotient:", quotient)

# In a larger program, a guard can prevent the rest of a calculation from
# running on invalid data. This example keeps the whole file runnable:
temperature_c = -5

if temperature_c < -273.15:
    print("Invalid temperature: below absolute zero.")
else:
    temperature_f = temperature_c * 9 / 5 + 32
    print(f"{temperature_c} C is {temperature_f:.1f} F.")

# Validation should check the actual requirements. For example, checking
# that a score is within 0..100 is different from checking whether it passes.
score = 104
if 0 <= score <= 100:
    if score >= 50:
        print("Valid score: pass.")
    else:
        print("Valid score: not passing.")
else:
    print("Invalid score: enter a value from 0 through 100.")


# ---------------------------------------------------------------------------
# 11. A decision table in code: shipping cost
# ---------------------------------------------------------------------------

# For multi-rule problems, write down the cases before coding. Here the
# shipping rule is:
#   * invalid weight (zero or negative): report an error;
#   * otherwise, weight through 2 kg: $5;
#   * otherwise, weight through 10 kg: $10;
#   * heavier packages: $20.
package_weight_kg = 6.5

if package_weight_kg <= 0:
    print("Package weight must be positive.")
elif package_weight_kg <= 2:
    shipping_cost = 5
    print(f"Shipping cost: ${shipping_cost:.2f}")
elif package_weight_kg <= 10:
    shipping_cost = 10
    print(f"Shipping cost: ${shipping_cost:.2f}")
else:
    shipping_cost = 20
    print(f"Shipping cost: ${shipping_cost:.2f}")

# Notice that the later thresholds do not repeat the lower bound. If execution
# reaches elif package_weight_kg <= 10, the earlier checks have already shown
# that the weight is greater than 2.
#
# Boundary testing is important. Try weights -1, 0, 2, 2.01, 10, and 10.01.
# These values exercise invalid input and both sides of each threshold.


# ---------------------------------------------------------------------------
# 12. The conditional expression
# ---------------------------------------------------------------------------

# For one simple choice of value, Python has a compact conditional expression:
#     value_if_true if condition else value_if_false
#
# It is an expression, so it produces a value that can be assigned or used in
# another expression. Read it as "value_if_true if condition; otherwise
# value_if_false."
items_in_cart = 1
item_label = "item" if items_in_cart == 1 else "items"
print(f"There are {items_in_cart} {item_label}.")

# Prefer a regular if/else when either branch needs multiple statements or
# when the expression becomes difficult to understand:
#
# if items_in_cart == 1:
#     item_label = "item"
# else:
#     item_label = "items"


# ---------------------------------------------------------------------------
# 13. Common conditional mistakes
# ---------------------------------------------------------------------------

# Mistake 1: using assignment instead of comparison.
# if score = 50:  # SyntaxError; use == to compare.
#     print("This is not valid Python.")

# Mistake 2: writing a mathematical range in a way that Python does not mean.
# The following does NOT check whether score is between 0 and 100:
# if 0 <= score <= 100:  # This is the correct chained comparison.
#     print("Score is in range.")
#
# Specifically, "0 <= score <= 100" is the readable, correct form. Avoid
# translating it into "0 <= score and score <= 100" unless that is clearer.
# A condition such as "score == 0 or 100" is not a range check; it compares
# score to 0, then uses 100 as a truthy value.

# Mistake 3: forgetting that elif checks in order. Put narrower/more specific
# cases before broad cases.

# Mistake 4: using separate if statements when the cases must be exclusive:
#
# if score >= 90:
#     print("A")
# if score >= 80:
#     print("B")
#
# A score of 95 would print both A and B. Use elif for mutually exclusive
# alternatives so that only the first matching branch runs.

# Separate if statements are appropriate when more than one action may apply:
is_weekend = True
is_holiday = True
if is_weekend:
    print("Weekend schedule applies.")
if is_holiday:
    print("Holiday schedule applies.")

# Mistake 5: comparing values of incompatible types. input() returns str, so
# compare or convert it deliberately:
# entered_age = input("Age: ")
# if entered_age >= 18:  # TypeError: string and integer cannot be ordered.
#     print("Adult")
# Correct approach:
# entered_age = int(entered_age)
# if entered_age >= 18:
#     print("Adult")


# ---------------------------------------------------------------------------
# 14. Optional interactive example
# ---------------------------------------------------------------------------

# Uncomment this section to try a decision using user input. input() returns
# text; int() converts that text to a whole number. The input must be a valid
# integer or int() will raise ValueError.
#
# entered_score = int(input("Enter a score from 0 to 100: "))
# if not 0 <= entered_score <= 100:
#     print("That score is outside the allowed range.")
# elif entered_score >= 50:
#     print("You passed.")
# else:
#     print("You did not pass.")


# ---------------------------------------------------------------------------
# 15. Practice: predict, then check
# ---------------------------------------------------------------------------

# Predict which message each example prints before looking at the result.

# Practice A: Exactly one of the if and else blocks runs.
practice_temperature = 12
if practice_temperature > 20:
    practice_a = "warm"
else:
    practice_a = "cool"
print("Practice A:", practice_a)

# Practice B: Which first matching grade condition is selected?
practice_score = 70
if practice_score >= 90:
    practice_b = "A"
elif practice_score >= 70:
    practice_b = "C"
elif practice_score >= 50:
    practice_b = "D"
else:
    practice_b = "F"
print("Practice B:", practice_b)

# Practice C: Work out the Boolean expression using parentheses.
practice_age = 17
practice_has_permission = True
practice_c = practice_age >= 18 or practice_has_permission
print("Practice C:", practice_c)

# Practice D: The branches are independent, so more than one message can run.
practice_is_student = True
practice_has_lab = True
if practice_is_student:
    print("Practice D: student")
if practice_has_lab:
    print("Practice D: lab access")

# Try these extensions:
#   * Change practice_temperature to 20. Is it warm or cool? Why?
#   * Add a boundary rule for a score of exactly 100 to the grade example.
#   * Write a decision that classifies a number as negative, zero, or positive.
#   * Make a simple ticket price decision using age ranges. Test the exact
#     boundaries as well as values just above and below them.
#   * Draw a flowchart or list of cases before writing the ticket decision.


# ---------------------------------------------------------------------------
# Key ideas to remember
# ---------------------------------------------------------------------------

# * Branching lets a program choose which statements to execute.
# * if tests a condition; elif tests another condition only if earlier ones
#   were False; else handles every remaining case.
# * Conditions evaluate to True or False. Comparisons commonly create them.
# * Indentation defines the statements inside a branch.
# * In an if/elif/else chain, at most one branch body runs.
# * Separate if statements are independent and may each run.
# * Condition order matters. Test specific cases before broad cases.
# * and, or, and not combine or reverse conditions; parentheses clarify logic.
# * Test boundary values and invalid inputs, not only typical examples.