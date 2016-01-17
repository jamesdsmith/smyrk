# smyrk 😏
smyrk is a programming language whose code is written entirely in emoji characters. Why? Why not!

## Language Syntax Guide

❌ (HALT)
* Exits the current runtime
* Status: Not started, need a way to signal from the runtime to the REPL that the program has ended

👉 (CONST)
* Pushes the parameter on to the stack
* Status: Complete

👀 (STO)
* Pop a value and store it into the parameter variable
* Status: Complete

🗄 (LOAD)
* Push the value stored in the parameter on to the stack
* Status: Complete

➕ (ADD)
* Pop two items on the stack, add them, push the result on to the stack
* Status: Complete

➖ (SUB)
* Pop two items off the stack, subtract them, push the result on to the stack
* Status: Complete, but it's current behavior may be considered to be backwards

✖️ (MUL)
* Pop two items off the stack, multiply them, push the result on to the stack
* Status: Complete

➗ (DIV)
* Pop two items off the stack, divide them, push the result on to the stack
* Status: Complete, but it's current behavior may be considered to be backwards

🤔 (EQL)
* Pop two items off the stack, push their equality in to the stack
* Status: Complete

🌚 (LSS)
* Pop two items off the stack and check if the first popped item is less than the second
* Status: Complete, but possibly backwards

🌝 (GTR)
* Pop two items off the stack and check if the first popped item is greater than the second
* Status: Complete, but possibly backwards

🏃 (JMP)
* Equivalent of a goto statement
* Status: Not started

🚶 (FJMP)
* Equivalent to an if statement
* Status: Not started

📖 (READ)
* Read an input from the user and push it to the stack
* Status: Not started, need to write a prompt for the input

🖨 (WRITE)
* Pop an item off the stack and print it to the screen
* Status: Complete

☎️ (CALL)
* Create a new environment with the current environment as its base, and run a function in the new environment
* Status: Not started

⚓️ (DEF)
* Define a function, store a series of commands to run them at a later date
* Status: Not started

🔙 (RET)
* Defines a return point from functions
* Status: Not started