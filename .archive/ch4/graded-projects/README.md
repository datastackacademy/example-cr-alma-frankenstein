## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Chapter Code Review 
In this project, you'll be using Flask to make an app that can GET and POST to an API. For simplicity, we'll skip the MariaDB database and just store our data in a Pandas DataFrame.

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include a README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Install Requirements
Create a `requirements.txt` file, and include the following packages:
```python
pandas==1.3.5
jupyterlab==3.4.2
Flask==2.1.2
PyYAML==6.0
PyMySQL==1.0.2
SQLAlchemy==1.4.36
```
Pip install the requirements.

### Instructions:

#### Code to Include
- In a `main.py` file:
1. Create a Pandas DataFrame to hold superhero stats. This will act as a mock database. You can fill in values in the snippet below:
```python
super_data = [
    {"name":  , "superpower":  , "weakness":  },
    {"name":  , "superpower":  , "weakness":  },
    {"name":  , "superpower":  , "weakness":  }
]
super_df  = pd.DataFrame(super_data)
super_df.set_index(keys="name", drop=False, inplace=True)
```
2. Create a Flask instance called "app"
3. Under the Flask instance, include this snippet to set the database:
```python
app.config["db"] = super_df
```
4. Use the `@app.route` decorator to create an endpoint of "/see_stats", with a method of "GET".
    - Under the decorator, write a function that allows a user to query by name, superpower, and/or weakness. 

5. Use the `@app.route` decorator to create an endpoint of "/add_stats", with a method of "POST".
    - Under the decorator, write a function that allows a user to add a new superhero. 
    - In the function, include an `if/else` statement that only includes the new superhero if name, superpower, and weakness are all present. If all three aren't there, the new entry isn't included in the database.
    - You can decide what the function will return to the user when the post is successful, and when it isn't.

6. Be sure to include the following snippet at the bottom of your `main.py` file, and test the app runs on localhost port 5050 when you run the file:
```python
if __name__ == '__main__':
    app.run('0.0.0.0', 5050)
```


### Accepting Criteria

Your submitted repository should:

1. Create a Flask API app that can be launched on a localhost.

1. Include the two endpoints listed above.

1. Allow users to query by name, superpower, and/or weakness.

1. Allow users to post a new entry only if all information is included.

1. Include a README, .gitignore, a requirements.txt, and at least 8 commits. Your code should be readable and well-commented.


#### Three Point Bonus
Access a public API and use a GET request to write a query for some of the data. In a notebook, include any code you wrote for your query, as well as a brief explanation of the API and what your query is looking for. Include the query results as a JSON or CSV file.

[API Ninjas](https://api-ninjas.com/) and [GitHub public-apis]( https://github.com/public-apis/public-apis) are both great places to find APIs to work with.
