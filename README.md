# Adoptopet
The nature of the dataset has inspired me to create my project with a real demand in mind. 

The problem: Pet owners looking for their lost pets will need to contact every rescue centre 
individually to check that their pet hasn't been taken in.

The solution: An online catalogue that is device independant, that allows people to search and
browse the union of pets from multiple pet centres. This can be used both by owners looking for 
lost pets, or new owners looking to adopt!

-------------Features------------------------
1)Specifically search pets by gender, species, colour, and name
2)Browse pets by popularity, and alphabetically (distance under works)
3)Request autocompletion for your current input
4)Upvote pets you think are cute. (this affects popularity)

--------------Scripts-------------------------
main.py will run the app

image_adder.py is a script that manipulates the dataset
it's used to assign a new column of image_id's to every
row depending on their colour. This id is used in the 
templates to display different coloured animals.

--------------How to run?----------------------
Install flask, and execute the main.py function to 
create a localhost. Head to localhost:5000 to see 
the app locallly.


Built in python 3.6.6 and Flask

