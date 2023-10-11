### DevOps Practice - _Task 1_

>Create a Python script to sort a list of numbers you pass to it using an environment variable. Implement two sorting algorithms of your choice as two different functions.

>The script will be stored in a git repository. Apply the trunk-based development flow to work on the repository.

>Containerise the script using Docker and add the Docker file to the repository.
You can choose which sorting algorithm to use to sort the list when the script is executed using an environment variable.

>Run the script using Docker by passing the required environment variables for the list of numbers and the sorting algorithm. The run should return the sorted list of numbers.

>Create a README.md file in the repository where you’ll document how the script works and how to run it using Docker and add a screenshot with a local execution of the docker image.

### Solution:
Please enter the command below and please change the "X" characters with:
-METHOD= 1 - Selection method, 2 - Insertion method
-LIST_NUMBERS="22, 34, 54, 30..." - comma separated numbers to be sorted.

Command:
docker run -e METHOD="X" -e LIST_NUMBERS="X,X,X,X" dockerfile

![Local execution of the script](https://github.com/NeluTriesIT/DevopsPractice/blob/master/task1_local.png?raw=true)
