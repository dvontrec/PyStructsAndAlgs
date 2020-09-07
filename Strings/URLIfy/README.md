## URLify

*Write a method to replace all spaces in a string with "%20" string has
sufficient space, and you are given the true string length*

- *Since we are working in python, we turn the string to an array then back*

- We will use 2 pointers

- Start P2 from the very end of the string

- Start P1 at the true string length

- Loop backwards until P1 is at the end
    - If char at P1 is a space
        - Replace P2 with 0 char
        - Decrease P2 by 1
        - Replace P2 with 2 char
        - Decrease P2 by 1
        - Replace P2 with % char
    - else 
        - Replace P2 with char at P1
    - Decrease P2
    - Decrease P1

- Return the string
