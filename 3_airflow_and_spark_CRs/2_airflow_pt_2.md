## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Airflow pt 2
For today's project, you'll be using Airflow to plan a party! Here's the story:

Your cohort, plus several dozen of your closest friends, want to celebrate learning Airflow. You've all been asked to vote on a cake flavor from the following list
```python
flavors_choices = ["lemon", "vanilla", "chocolate", "pistacio", "strawberry", "confetti", "caramel", "pumpkin", "rose"]
```
The votes are tallied in a `.csv` file stored on BigQuery.
 
You'll use decorators, a file connection and file sensor, and XComs to check when the votes CSV has been uploaded to your local filesystem, then find the flavor with the most votes.

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Instructions:
1. Set up your project by including:

    - folders for `dags/`, `plugins/`, `logs/`, and `data/`

    - a `.env` file with the variables `AIRFLOW_UID` and `AIRFLOW_GID` set to the current user

    - a `.gitignore` file to ignore the `plugins/` and `logs/` folders, the `.env` file, the contents of the `data/` folder, and the virtual environment.

    - a `docker-compose.yml` file

1. Create a file connection called `data_fs`. Include a note in your `README` telling your users how to do this, too.

1. Write a DAG that:

    - Uses a file sensor to check whether the `votes.csv` file has been uploaded to the `data/` folder of this repository.

    - Has a task that reads each row in `votes.csv`, and checks whether that value is in the `flavors_choices` list defined above. If it is, append it to a new list called `valid_votes`. This task should return the `valid_votes` list.

    - In another task, use a Python function that takes a list as an argument, and prints the item that appear the most times in that list.

1. Pass the `return_value` XCom from the first task as an argument to the second task.

1. Use decorators to define the tasks.

1. You can copy the votes CSV to your local system with the command
```bash
gsutil -m cp gs://data.datastack.academy/airflow_cr_2/votes.csv .
```

### Accepting Criteria
- The project includes an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.
- The README has instructions for how your user can set up and run the project, including:

    - Cloning the project from GitHub

    - The `docker-compose` commands needed to start Airflow

    - Instructions on how to create a file connection for the `data/` folder

    - The command for copying `votes.csv` to their local system

- The README includes a diagram of your DAG (a screenshot from the Airflow GUI or an illustration with draw.io is okay).
- The DAG uses XComs, decorators, and a sensor, and follows the instructions above.
- The project can run successfully on the Airflow GUI.
- The project is well-commented, without unused code.