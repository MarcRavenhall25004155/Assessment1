# Register Program
# Overview
This program allows users to create a simple register by entering names.
Each name is automatically stored with the exact date and time it was added.
The register is displayed in alphabetical order to the user once they finish adding entries.

# How to run
* Make sure python 3 is installed
* Save the script as 'main.py'
* Open a terminal or command prompt
* Run using 'python main.py'
# How to use
* Enter a name when asked
* The system will ask if you want to enter more names. Select y/n
* Once you have finished entering names select 'n'. The program will display the full register.
## Example
When you run the code you will see prompts like this:
```
===Create a Register===
Enter a name: Doe, John
Would you like to enter another name?(y/n): y
Enter a name: Doe, Jane
Would you like to enter another name?(y/n): n

===Register===
Doe, Jane - 2025-12-17 22:59:10
Doe, John - 2025-12-17 22:58:00

===End of List===
