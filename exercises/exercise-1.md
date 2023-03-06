# Exercise 1

**Requirement 1.** Create new file named `calc.py`

**Requirement 2.** Build a console program that prompts the user for a command.

Seven Commands:

- add: add a new operand to the current result
- subtract: subtract a new operand from the current result
- multiply: multiply a new operand from the current result
- divide: divide a new operand from the current result
- exponent: raise the current result to the power of a new operand
- clear - reset current result to 0
- exit - exits the program

Prompt the user for the command and the operand.

- Enter a command: add
- Please enter an operand: 10

**Requirement 3.** Display the result after each command.

- Result: <previous result + 10>

**Requirement 4.** If the user types no command, display the following error message: "Invalid Command, Try Again."

**Requirement 5.** Using a list of dictionaries, capture a history of the calculator commands: add, subtract, multiple, divide, exponent

For each history entry, store a unique integer id (do not use external modules, just write some code to generate an id), the name of the command, and the operand value typed in. Do not track the result on the history.