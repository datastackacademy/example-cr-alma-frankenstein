## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: JSON, Advanced Python, and Working with Files
Today, you'll make a finished pipeline drawing on all the skills you've learned so far. Please pay close attention to the directions!

### Instructions:
1. Use Python's `Faker` library to generate a list of twenty colors. Call it `color_list`.
> Just like you generated names with `fake.name()` in chapter 3, episode 1, you can generate colors with `fake.name()`, once you've imported Faker and created a `fake` class. 
- Write a function to remove any duplicates from `color_list`.
- Once `color_list` only has unique values (no duplicates) use a dictionary comprehension to create a dictionary from it. Each value should be the name of the color, and its key should be the length of the name. Call it `color_dict`.
> For instance, the list `["pink"]` would create the dictionary `{"pink": 4}`, because the word "pink" has four letters.
- Write `color_dict` into a JSON file. Include this file in your GitHub repository.
- Read the `color_dict` back out of the JSON file. If the value is 4 or more, print a string saying the color name and the length of the name.


### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Accepting Criteria
The project should:
- Include informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.
- Be well-commented, without unused code.
- Generate a list using Faker.
- Remove duplicates from the Faker list.
- Use a dictionary comprehension as outlined above.
- Write the dictionary to a JSON file.
- Read the dictionary back out, and print strings of the keys that have 4 or more characters.
