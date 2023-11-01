## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Airflow 1
For this project, you'll be making a simple DAG that your user can run on the Airflow graphical interface. It will use Bash to echo your name, save the echoed value as a text file, then use Python to read and print the value in that file. Then, it will run three simultaneous tasks that each print a different random value. The DAG will finish with an empty operator.

### Setup Git
1. As always, create a repository on GitHub for this project. 

2. Include a README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Install Requirements
- Include whatever dependencies you need in your requirements.txt (see the Airflow episodes for reference).
 
- Create a virtualenv, activate it, install Airflow, then install the dependencies in your `requirements.txt` file, just like we've been doing in class.


### Project Setup
In a folder in your repository:

- Create the following directories: 'dags', 'logs', and 'plugins'

- Create a .env file that sets the 'AIRFLOW_UID' to the current user's ID (you can get this by typing `id -u` into the terminal.)

- Download the docker-compose.yml from [https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)

- In the dags directory, create a file for your DAG called `code_review.py`

### Instructions for the DAG:

- In the `code_review.py` DAG, include the needed imports, and create default arguments for your DAG.
 
- Include, near the top of your code, the following constant:
```
APPLES = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]
```

- Instantiate a DAG with a name, description, and the default args.

- Give your DAG the following tasks:

    - Task 1. A `echo_to_file` task that uses a Bash operator. This task should echo your name, and redirect the output into a file called `code_review.txt` that's in the same directory as the `code_review.py` file    

    - Task 2. A 'greeting' task that uses a Python operator to call a Python function called `print_hello()`. `print_hello()` will need to be defined above the DAG. It should open `code_review.txt`, read your name from that file, and print a greeting that includes your name.
    
    - Task 3. A task using a Bash operator, which echos "picking three random apples".
    
    - Tasks 4, 5, and 6 are three Python operator tasks that will run simultaneously. Each task should:
    
        - Have a unique task ID
        
        - Use a `python_callable`. This function should randomly select an apple from the `APPLES` list, put it into a string, and print that string
            
    - Task 7. End the DAG with an empty operator.

- The tasks should run in the order listed above, with task 4-6 running simultaneously.


### Accepting Criteria

Your submitted repository should:

- Include a README with instructions for the `docker-compose` commands that your user should use to run the DAG in the Airflow GUI, a diagram of your DAG (a screenshot from the Airflow GUI or an illustration with draw.io is okay), and an explanation of the project.

- Have well-commented code, at least 8 commits, and no unused code

- Run successfully on the Airflow GUI

- Have a DAG with the tasks outlined above, and the tasks should run in the order specified

- Include the following files: 'requirements.txt', '.gitignore', and a 'dags' directory.

