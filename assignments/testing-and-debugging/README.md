# 📘 Assignment: Testing and Debugging Python Programs

## 🎯 Objective

Learn how to use `pytest` to check Python functions and find bugs. You will write tests for normal and edge-case inputs, then use failing tests to improve a small program.

## 📝 Tasks

### 🛠️ Write Tests for Functions

#### Description
Create a test file named `test_starter_code.py` and write tests for each function in `starter-code.py`. Use `pytest` assertions to describe the results the functions should produce.

#### Requirements
Completed program should:

- Include at least two tests for each function.
- Test normal inputs and at least one edge case.
- Use clear test function names that describe the behavior being checked.
- Run successfully with `pytest` after the bugs have been fixed.

### 🛠️ Find and Fix Bugs

#### Description
Run the test suite, read the failure messages, and correct the defects in `starter-code.py`. Keep rerunning the tests until the complete suite passes.

#### Requirements
Completed program should:

- Correctly determine whether an integer is even.
- Count vowels in a string without treating consonants as vowels.
- Return a helpful result when `safe_divide()` receives a zero divisor.
- Pass all student-written tests without changing the tests to hide failures.

### 🛠️ Improve Test Coverage

#### Description
Review your tests and add cases that protect the program from regressions. Explain what each edge case checks in a short note in your submission.

#### Requirements
Completed program should:

- Test zero and negative values for `is_even()`.
- Test an empty string and a string with mixed uppercase and lowercase letters for `count_vowels()`.
- Test both successful division and division by zero for `safe_divide()`.
- Include a short written explanation of one failure message and the fix it led you to make.