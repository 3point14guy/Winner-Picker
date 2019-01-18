# Winner Picker

Winner Picker is a command line program that randomly generates a winner from a list of user generated names.

To use Winner Picker, fork and clone this repo and run ```python winner_picker.py``` from the command line.

Winner Picker has a ```names.txt``` file with a default list of names to test the program's functionality without entering your own list.

To enter your own list, first use the Remove Names feature to wipe the file and then proceed to Add Names to build your list.



The Asheville Chapter of Google Developers Group held a 5 part Intro to Python course from November 2018 through January 2019. The course was facilitated by Daryl Rue and used Udacity's [Introduction to Python Programming](https://www.udacity.com/course/introduction-to-python--ud1110) as the lesson material.

Winner Picker is my solution to the course final project.

The reuirements for that final project:

For this class you will complete your final project. You can choose between the following 2 options:
* Create your own program. You design and build any program you choose. The only requirement is that it is written in Python.
* Pick a Winner This is a console version of the online Roulette wheel that picks a winner from a list of names. The requirements are:
  * You must read the list of names from a text file.
  * You must include some basic console user commands like "add Bob Smith," "remove Sally Southerland," and "list"
  * When the user enters the command to pick a winner (let's say it's "pick winner"), the program must randomly pick a winner from your list of entrants, display it to the console, and remove that entrant from the list.
  * Make sure you handle basic error cases, such as when a user enters "pick winner" and there are no entrants, or when a user enters "remove Frank Williams" and Frank Williams isn't on the list.
  * Make sure you give the user the ability to end the program (such as entering 'q').
