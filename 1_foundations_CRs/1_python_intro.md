## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Intro to Python
For today's code review, you'll be writing several functions that show off your skills using dictionaries, loops, lists, and strings.

### Instructions:
Please stick to the function names given below, so that the code review can be graded with automated testing.

Write the following in a file called `main.py`:
1. A function called `list_sayer()` that takes a list as an argument
    - If the list isn't empty (i.e. there's one or more items in it):
        - print a string for each item saying the name of the item and its index
        - return the Boolean `True`
    - If the list is empty:
        - print a string saying that the list is empty
        - return the Boolean `False`

1. A function called `dict_sayer()` that takes a dictionary as an argument
    - If the dictionary isn't empty (i.e. there's one or more items in it):
        - print a string for each item saying the name of each key and its value
        - return the Boolean `True`
    - If the dictionary is empty:
        - print a string saying that the dictionary is empty
        - return the Boolean `False`

1. A function called `greatest()` that takes as an argument a dictionary that has strings and keys and integers as values
    - find the greatest value
    - return a tuple with the greatest value and its key

1. A function called `zipper()` that takes two lists as arguments
    - If the lists are the same length:
        - return a dictionary that has the items of the first list as keys, and each item in the same index in the second list as the value
        > For instance, the lists `["vanilla", "cherry"]` and `["cake", "ice_cream"]` would return `{"vanilla": "cake", "cherry": "ice_cream"}`
    - If the lists are different lengths:
        - return a tuple with each list and its length
        > For instance, the lists `["vanilla", "cherry", "pistachio"]` and `["cake", "ice_cream"]` would return `(["vanilla", "cherry", "pistachio"], 3, ["cake", "ice_cream"], 4)`

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Accepting Criteria
- Include informative README, a `.gitignore` file and at least 8 commits.
- The project should be well-commented, without unused code.
- `list_sayer()` is completed, and runs according to the specs.
- `dict_sayer()` is completed, and runs according to the specs.
- `greatest()` is completed, and runs according to the specs.
- `zipper()` is completed, and runs according to the specs.