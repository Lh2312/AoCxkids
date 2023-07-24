## Day 1: Not Quite Lisp 
### https://adventofcode.com/2015/day/1 

Santa is trying to deliver presents in a large apartment 
building, but he can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), 
means he should go down one floor.

##Part 1: To what floor do the instructions take Santa?
my answer: 138
 
open the input and read it. Your input is a long long line of parentheses,
representing floors, choose an appropriate VARNAME1
``` python
filename=open("C:\\...\\2015Day1.txt", "r") 
VARNAME1 = filename.read()
```
you need a counter to keep track of what floor Santa is VARNAME2. 
Santa starts on floor 0, choose an INT to assign to your VARNAME2
``` python
VARNAME2 = INTEGER
```
you need to loop through each symbol in your input, choose a VARNAME3 that will represent each step
``` python
for VARNAME3 in VARNAME1:
```
what happens if the symbol is "("?
you need to increase your VARNAME2 by 1 floor
remember that a STATEMENT is a logical condition that can be == (equal), != (not equal), > (greater than) etc.
``` python 
   if (STATEMENT):
        INCREASE VARNAME2 by 1
```
Else if the symbol is ")", you need to decrease VARNAME2
``` python
    elif (STATEMENT):
        DECREASE VARNAME2 by 1
```
you can now print your VARNAME2 and submit your answer :)
``` python
print (VARNAME2)
```
## Part 2: Now, given the same instructions, find the position of the first character that causes him to enter 
the basement (floor -1). 
The first character in the instructions has position 1, the second character has position 2, and so on.
Example: ()())
position 1: ( -> floor 1
position 2: ) -> floor 0
position 3: ( -> floor 1
position 4: ) -> floor 0
position 5: ) -> floor -1

my answer: 1771

you need a new variable to keep track of the symbols' position
add VARNAME4=INT right after VARNAME2=INT
Pay attention to the text: "The first character in the instructions has position 1"
and choose an appropriate first value
``` python
VARNAME2=INT
VARNAME4=INT
```
go to your for loop, it should look like this:
``` python
for VARNAME3 in VARNAME1:
    if (STATEMENT):
        INCREASE VARNAME2 by 1
    elif (STATEMENT):
        DECREASE VARNAME2 by 1
 ```       
add an IF statement that checks if Santa is on floor -1
Your statement should check if VARNAME4 is == -1
``` python
    if (STATEMENT):
```
if the statement is true, Santa is on floor -1
and you can just print your VARNAME4 to find the position
``` python
        print(VARNAME4)
```
you don't need to proceed any further, so you can BREAK out of the loop
 ``` python
       break
```
finally, don't forget to update your VARNAME4 after the IFs but still inside the FOR :)
``` python
    VARNAME4+=1
```

## CODE WITHOUT COMMENTS

``` python
# part 1
filename=open("C:\\...\\2015Day1.txt", "r") 
VARNAME1 = filename.read()

VARNAME2 = INT

for VARNAME3 in VARNAME1:
    if (STATEMENT):
        INCREASE VARNAME2 by 1
    elif (STATEMENT):
        DECREASE VARNAME2 by 1

print (VARNAME2)

# part 2
VARNAME2=INT
VARNAME4=INT

for VARNAME3 in VARNAME1:
    if (STATEMENT):
        INCREASE VARNAME2 by 1
    elif (STATEMENT):
        DECREASE VARNAME2 by 1
    if (STATEMENT):
        print(VARNAME4)
        break
    VARNAME4+=1
```
## WORKING CODE

``` python
# part 1
filename=open("C:\\...\\2015Day1.txt", "r") 
floors = filename.read()

SantaPos = 0

for floor in floors:
    if (floor=="("):
        SantaPos+=1
    elif (floor==")"):
        SantaPos-=1

print (SantaPos)

# part 2
SantaPos = 0
pos = 1

for floor in floors:
    if (floor=="("):
        SantaPos+=1
    elif (floor==")"):
        SantaPos-=1
    if (SantaPos==-1):
        print(pos)
        break
    pos+=1
```
