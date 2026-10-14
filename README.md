# EECS 1011 Lecture Notes

Personal, code-focused notes and examples for studying topics in EECS 1011.
The repository is organized so that each topic can be read and run as a
standalone Python file.

> **Note:** These are student study notes, not official course materials.
> Always use the course outline, instructor announcements, and assigned
> resources as the authority for course requirements.

## Contents

### Midterm review

| Topic | File | What it covers |
| --- | --- | --- |
| Variables, types, and expressions | [`midterm/Variables, Types & Expressions.py`](midterm/Variables%2C%20Types%20%26%20Expressions.py) | Variables, Python's basic types, arithmetic and text expressions, comparisons, Boolean logic, conversions, and common mistakes |
| Branching and conditionals | [`midterm/Branching & Conditionals.py`](midterm/Branching%20%26%20Conditionals.py) | `if` / `elif` / `else`, Boolean conditions, nesting, short-circuiting, validation, and boundary cases |
| Loops and iteration | [`midterm/Loops & Iteration.py`](midterm/Loops%20%26%20Iteration.py) | `for` and `while`, `range()`, accumulators, filtering, `break`, `continue`, nested loops, and loop errors |

Topics may be added or reorganized as the notes grow.

## Getting started

The examples are written for **Python 3** and use only the Python standard
library. To run a lesson, open a terminal in the repository folder and execute
the file. For example:

```bash
python "midterm/Branching & Conditionals.py"
```

On some systems, the Python command may be `python3` instead:

```bash
python3 "midterm/Branching & Conditionals.py"
```

On Windows PowerShell, this path form also works:

```powershell
python "midterm\Branching & Conditionals.py"
```

Run the other lessons by replacing the filename. The notes are designed to
run from top to bottom; some interactive input examples are commented out so
the complete file can run without waiting for input. Uncomment those examples
when you are ready to try them.

## How to use these notes

1. Read the explanation and comments in a topic file.
2. Before running an example, predict what it will do.
3. Run the file and compare the output with your prediction.
4. Change the example values and run it again to test your understanding.
5. Try the practice prompts at the end of each lesson, then check edge cases
   such as empty input, boundary values, and unexpected types.

The examples are teaching material: they favor clarity and explicit steps
over compact or production-oriented code.

## Contributing to your notes

When adding a topic, a self-contained Python file with descriptive headings,
comments, runnable examples, and practice prompts helps keep the repository
easy to study. Keep examples appropriate to the concepts already introduced,
and verify that each file runs before adding it.
