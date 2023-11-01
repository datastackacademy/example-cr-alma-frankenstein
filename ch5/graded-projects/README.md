Project Overview

In this project you will create a docker-compose script that will replay the first telephone conversation between Alexander Graham Bell and Thomas Watson. The docker-compose will contain 2 containers: one for Bell and one for Watson. The Watson container will use the Python `flask` module to serve an API awaiting for messages to be received and replying with responses. The Bell container will contain use the python `request` module to send messages to Watson. The Bell container should initiate the conversation. The file `/data/bell.txt` and `/data/watson.txt` contain the messages and responses sent back and forth. 

In this exercises you will demonstrate your ability to:

- Create python scripts using `flask` and `requests` showcasing a REST server and request calls
- Develop a _state machine_ that carries out a conversation. State machines are a programming technique used when you need to coordinate a series of steps between two or more programs. This ensures that each program, Bell and Watson, carry out their conversation in sequence; speaking their sentences in sequence only after one has heard the other's message.You can read more about _state machines_ [here](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/).
- Read sentences between Bell and Watson from data files
- Create a Dockerfile container encompassing your scripts
- Develop a docker-compose script which runs both containers in sequence:
  - You must ensure that the Bell container runs only after Watson is fully functional and ready to receive
- Print the full conversation between Watson and Bell

​

## Setup git

For this graded assessment, create a new Git project to store your code. As you write your code to meet the accepting criteria below, commit your files to this repo _and_ update the README.md to provide information about the organization and use of the code you're writing.

## Data

The files `data/bell.txt` and `data/watson.txt` contain the sentences spoken between _Bell_ and _Watson_. Each container must send all their sentences in sequence, meaning:

- Bell will send the first line
- Watson responds with their first line
- Bell sends their second line
- Watson replies
- ...
- Until both Bell and Watson have transmitted the entire content of their files

## Src

The `src/` dir contains  two starter files to serve as the basis for your Bell and Watson. 

## Acceptance Criteria

1. Correctly finishing both Watson and Bell python code. Your code must:
   1. Have a functional flask app.
   1. Make REST request calls.
   1. Read messages from data files.
   1. Print received messages to console.
   1. The host/port for Watson must be passed to Bell's code as environment variables.
2. Create a Dockerfile for both Bell and Watson
   1. Install required pypi packages.
   2. Set Watson's host/port in Bell's container as environment variables.
   3. Expose Watson's flask port (8081).
   4. Use a Dockerfile `CMD` command for Bell and an `ENTRYPOINT` for Watson.
3. Create a bash/shell script that:
   1. Runs both Watson and Bell containers sequentially in this order.
   2. Attaches the data directory containing the files as data volumes to both containers.
   3. Runs Bell only after Watson is fully functional (listening on port 8081). You can implement a sleep cycle in the bash to ensure Watson is up and running first.
4. Demonstrate that messages between Bell and Watson are printed in sequence to the console.

**Optional: Additional Challenges**

You can implement none, one, or more of these options:

1. Create a docker-compose file which:
   1. Attaches the data directory containing the files as data volumes to both containers.
   2. Runs Bell only after Watson is fully functional (listening on port 8081).
1. Develop a healthcheck script (.py) for Watson and use it with docker-compose `HEALTHCHECK` and `depends_on` tags.
1. Create a third mariadb container. Enhance Watson container to log messages received into a database table. You can use either sqlalchemy or pandas. 
1. Enhance Watson to use [gunicorn](https://gunicorn.org/) server
