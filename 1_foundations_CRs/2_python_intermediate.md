## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Python Intermediate 1

### Instructions:
Please stick to the function names given below, so that the code review can be graded with automated testing.

Write the following in a file called `main.py`:
1. A function called `fourth_place()` that takes a list as an argument
    - it should return the fourth item in the list
    - use `try/except` to catch `IndexError`s

1. A lambda function that takes the two integers as arguments, and subtracts the second number from the first
    - assign a variable called `subtracter_lambda` to the lambda function
    - below the variable assignment, call `subtracter_lambda`

1. A class called `Shoe` that has the following attributes:
    - `US_size`: an integer
    - `color`: a string
    - `smelly`: a Boolean

    - `Shoe` should also have a method called `euro_size()` that converts `US_size` to European sizing by adding 33, and prints a string saying Euro size 
    - below the class definition, create an instance of `Shoe`
    - call the `euro_size()` method on your instance

1. Write a function called `galaxy()`. `galaxy()` should take:
    - a positional argument of the user's home planet, followed by
    - a varying number of arguments, and
    - a keyword argument of `pluto_is_planet`, which defaults to a Boolean of your choice

    - `galaxy()` should put all the arguments into a string, and return that string

    - below the function definition, call `galaxy()`. For the varying number of arguments, name as many planets as you can

1. Include type hints and docstrings in each function.

1. Use Pytest to write unit-tests for your each of functions.


### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Accepting Criteria
- Include informative README, a `.gitignore` file, and at least 8 commits.
- The project should be well-commented, without unused code.
- The function `fourth_place()` is completed, and runs according to the specs.
- The lambda function is completed, the variable `subtracter_lambda` is assigned to it, and it runs according to the specs.
- The `Shoe` class is completed, and runs according to the specs.
- The function `galaxy()` is completed, and runs according to the specs.
- All functions include type hints and docstrings.
- There's a Pytest for each of the functions.

### Bonus Point:
The lesson on unit-tests only went over testing functions, not classes. For a bonus point, write a test for the `euro_size()` method of your `Shoe` class.