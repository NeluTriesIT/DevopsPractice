Task1:
Create a Python script to sort a list of numbers you pass to it using an environment variable. Implement two sorting algorithms of your choice as two different functions.
The script will be stored in a git repository. Apply the trunk-based development flow to work on the repository.
Containerise the script using Docker and add the Docker file to the repository.
You can choose which sorting algorithm to use to sort the list when the script is executed using an environment variable.
Run the script using Docker by passing the required environment variables for the list of numbers and the sorting algorithm. The run should return the sorted list of numbers.
Create a README.md file in the repository where you’ll document how the script works and how to run it using Docker and add a screenshot with a local execution of the docker image.

Solution:
Please execute the following command in the terminal, once you have downloaded the script and the Dockerfile from this repo:
NOTE!:Change the "X" character from the METHOD env var with "1" for selection sort or "2" for insertion sort. 
      Change the "X" characters from the LIST_NUMBERS env var with the numbers you want to sort.
Command>
docker run -e METHOD=X -e LIST_NUMBERS="X,X,X,X,X" dockerfile
