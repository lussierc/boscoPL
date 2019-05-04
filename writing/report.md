# CS401 Project - Final Report
### Zachary Andrews, Devin Spitalny, Christian Lussier

## Introduction
For our CS401 Final Project, we decided to create a toy programming language,
much like the ones discussed in class. When coming up with a name for our simple
language, our minds immediately jumped to the lovable dog and unofficial
Allegheny Computer Science mascot, Bosco. With this in mind, we set about
creating our new Bosco programming language, drawing inspiration from other
languages such as Java and Python as well as toy languages such as Decaf and
C0. We created a basic grammar for our language with dog-related elements,
including dog phrases like "woof" and "bone" to add a dog flair of sorts.
Additionally, we also took steps to create a simple scanner/parser for our
language. When creating Bosco, we tried to create a fun and easy to understand
grammar that would work well with our scanner and parser.

## Project Motivation
<!-- The motivation for your project. Why is the problem you decided to solve important/useful? -->
When deciding on what to create for our compiler-related CS401 final project,
there were a number of motivating factors involved. While in class one day,
Professor Jumadinova mentioned the idea of making a programming language for our
final project, as it would be compiler-related. Our group was a little tentative
on this at first, but we were motivated to pursue this idea because creating our
own programming language sounded like a really cool idea. Once we had decided to
create a programming language, we were also motivated to make a fun and simple
language. Eventually, we came up with the idea of naming it Bosco and from
there, making a programming language with dog-related elements provided the fun
portion of motivation that we were looking for.

Additionally, once we had decided to make a toy or mini programming language,
we were motivated by many of the toy-programming languages that already existed.
"Trump Script" probably motivated us the most in this regard, because it was a
fun and playful programming language, based on many of Donald Trump's speaking
habits, that kind of exemplified what we wanted our programming language to be
in a way (except ours is dog-related instead of Trump-related). We were also
motivated by the mini-programming languages that students were using for their
compiler labs in class. The one that influenced and motivated us the most was
likely Decaf because we found it cool that it was basically a mini programming
language for Java and C#. Additionally, all of the project's group members had
used Decaf for their compilers.

## Background Information
<!-- Background for the proposed problem. What have others done for it already? Include references. -->
While our programming language doesn't solve a specific, real-world applicable
problem, it is an attempt to solve the problem of a lack of fun elements
existing in many programming languages. Our group feels that in most mainstream
languages, there just aren't many fun elements though this makes sense because
these languages are being used for real-world work. Many people seem to feel
similarly, as many toy programming languages have been created in recent years.

There actually are already dog-inspired programming languages that are publicly
available. However, until the week before the report was due, we had no idea
that a dog-related toy programming language existed. Despite this, there is a
language called ["DOG"](https://esolangs.org/wiki/DOG) which is very much
dog-related. Created by Jeremy Ruten, the programs for this language use
commands that are supposed to look like commands that you would give to a dog.
For instance, "fetch" is used to add, "drop" is used to subtract, and "bark" is
used to print. It is extremely simple, with no real mainstream formatting,
unlike that which appears in Java such as the use of brackets ({}) to denote
where the body of methods and classes appear.

As mentioned earlier, one other fun-inspired programming language is Trump
Script. Trump Script is based on Donald Trump phrases and speaking habits. While
it is not super-functional by any means, it is quite interesting and fun if you
follow American politics. In this sense, it was a motivation for our program, as
it strived to create a fun and real-world relevant programming language.

### References:
- "DOG" Programming Language: https://esolangs.org/wiki/DOG
- Trump Script: https://github.com/samshadwell/TrumpScript

## Overview of Completed Work
<!-- Detailed description of the work you completed for this project. Without giving a snap- shot of the code you wrote, describe what you implemented and how you implemented it. -->
Once we finalized the idea for our project, we completed work in a variety of
different areas. The first of these areas was creating a grammar for our
project. We took the time to create a grammar (that Bosco himself would love)
that contained a lot of whimsical dog-related elements. For example, our
reserved keywords included `woof`, `bone`, `speak`, `dig`, `treat`, `double`,
`fetch`,`goodboi`, `noise` and more. For instance, `woof` will be used for classes, `bone`
will be used for functions, `speak` will be used to print things to the
terminal, and `dig` will be used as a simple loop (like a for loop). In terms
of types, `treat` represents an integer, `goodboi` represents a boolean, and
`noise` represents a string. These keywords will play a large role in program
structure and functionality. Additionally, we also decided that `??` would be
used to denote single-line comments (because Bosco gets a little bit confused
sometimes).

Once we completed creating our grammar, we wrote a sample program for the Bosco
language to get a general idea of how it would function. This first sample
program, entitled `basicSyntax.bsco` included loops, functions, and variable
declarations. With this, it included some simple mathematical operations on
these variables and `speak` statements to print output to the terminal.

After finalizing our grammar and writing a sample program, we began the
implementation portion of our project. This involved implementing a scanner and
parser for our new Bosco language to use with our created sample programs. To
start, we began by determining which language to use for the implementation of
our scanner and parser. Eventually, we decided to use Python along with PLY (a
tool for easier scanning/parsing), as two of the group members had not used
Python for their compiler project and were interested in learning more. We first
began by defining our reserved keywords and tokens within the Python program. We
then began to define the values that could exist within a specified token and
the related elements of these tokens. After this, we began to implement our
created grammar into the program. We also added error handling and handling for
unspecified tokens/elements that may exist in incorrect Bosco programs.

After this, we were able to begin testing our scanner with our created sample
programs and found that it functioned as intended (more detail about the results
of our scanner appear in the next section). Later on, we activated the parser
functionality and ran into a number of issues. For the next week or two, our
group met several times to try and fix these parser issues. We did this by
having our parser display more advanced errors to see what the bug might have
been. Then based on these bugs we would change things in the program relating to
these bugs in an attempt to solve them, meaning we used a trial-and-error
approach to try and fix these bugs. Additionally, we looked through all of the
implementation details of the keywords, grammar, scanner, and parser in the
program code several times to look for error-causing code and discrepancies.
This is where we discovered the main source of our issues, a section of our
grammar was very ambiguous and could lead to incorrect tokens being added to
the stack which would then be unable to be simplified. To fix this we had to
make a change to all of the areas in our grammar that matched this kind of
issue, which after identifying was a very quick and easy process in comparison
to the hours we spent trying to figure out what was wrong.

## Overview of Results
 <!-- Description of your results. Make graphs, tables, snapshot of output, or anything else that can help me understand your results. -->
While completing this project and completing a variety of work, we produced a
variety of mixed results. The first of these was the successful creation of a
grammar with dog-related elements.

The Bosco Grammar:
```
Program ::== Decl+
Decl ::= BoneDecl | WoofDecl | VarDecl
WoofDecl ::= woof ID : Field* :
BoneDecl ::= bone ID - Formals - StmtBlock
Var ::= Type ID
VarDecl ::= Var\|
StmtBlock ::= ( VarDecl* Stmt* )
Stmt ::= 〈Expr〉 \| | IfStmt | DigStmt | BreakStmt | ReturnStmt | SpeakStmt | StmtBlock
Field ::= VarDecl | FuncDecl
Formals ::= Variable+, | ε
SpeakStmt ::= Speak- Expr+, \|
IfStmt ::= if ( Expr ) Stmt 〈else Stmt〉
ReturnStmt ::= return〈Expr〉\|
BreakStmt ::= break\|
DigStmt ::= dig Expr| Expr | Expr StmtBlock
Expr ::= LValue = Expr | Constant | LValue | ( Expr ) | Expr+Expr | Expr-Expr | Expr*Expr | Expr/Expr |
 Expr%Expr | - Expr | Expr < Expr | Expr <= Expr | Expr > Expr | Expr >= Expr | Expr == Expr |
 Expr != Expr | Expr && Expr | Expr || Expr | ! Expr | FetchTreat ( ) | FetchNoise ( )
LValue ::= indent (Actuals) | Expr . indent (Actuals)
Actuals ::= Expr+, | ε
Type ::= treat | double | goodboi | noise
Constant ::= treat | double | goodboi | noise | null
```

After creating our grammar, we worked to create a scanner and parser utilizing
it. Getting the parser to work properly was a hard process that took a lot of
trial and error to get working. Ultimately, we discovered that the issue we had
with our parser was due to how we had constructed our grammar. To fix this we
modified what we had used for a few of the statements that make up our grammar
and made the change in our parser as well. This fixed all of the issues we had
been having up until that point with the parser and allowed us to find other
areas that had similar issues.

Below is the current output from running the scanner/parser combination on
`basicSyntax.bsco`. Please note that the dots in the middle of the parsing
portion are there for the sake of saving space in the report and that the
program does parse correctly, the full output for the scanning/parsing of this
program can be found in `output/output_basicSyntax.txt`.

Sample Output:
```
LexToken(WOOF,'woof',2,42)
LexToken(ID,'classBosco',2,47)
LexToken(COLON,':',2,57)
LexToken(BONE,'bone',3,61)
LexToken(ID,'myFunction',3,66)
LexToken(MINUS,'-',3,77)
LexToken(MINUS,'-',3,78)
LexToken(RPAREN,'(',3,80)
LexToken(TREAT,'treat',4,86)
LexToken(ID,'x',4,92)
LexToken(ASSIGN,'=',4,94)
LexToken(TREAT,'2',4,96)
LexToken(BAR,'|',4,97)
LexToken(TREAT,'treat',5,103)
LexToken(ID,'y',5,109)
LexToken(ASSIGN,'=',5,111)
LexToken(TREAT,'17',5,113)
LexToken(BAR,'|',5,115)
LexToken(TREAT,'treat',6,121)
LexToken(ID,'z',6,127)
LexToken(ASSIGN,'=',6,129)
LexToken(ID,'x',6,131)
LexToken(PLUS,'+',6,133)
LexToken(ID,'y',6,135)
LexToken(BAR,'|',6,136)
LexToken(SPEAK,'speak',7,142)
LexToken(MINUS,'-',7,147)
LexToken(ID,'z',7,148)
LexToken(BAR,'|',7,149)
LexToken(LPAREN,')',8,199)
LexToken(COLON,':',9,201)
=======Parsing=======
PLY: PARSE DEBUG START

State  : 0
Stack  : . LexToken(WOOF,'woof',12,42)
Action : Shift and goto state 7

State  : 7
Stack  : WOOF . LexToken(ID,'classBosco',12,47)
Action : Shift and goto state 18

State  : 18
Stack  : WOOF ID . LexToken(COLON,':',12,57)
Action : Shift and goto state 22

State  : 22
Stack  : WOOF ID COLON . LexToken(BONE,'bone',13,61)
Action : Shift and goto state 8

State  : 8
Stack  : WOOF ID COLON BONE . LexToken(ID,'myFunction',13,66)
Action : Shift and goto state 19

....

State  : 1
Stack  : Program . $end
Done   : Returning <NoneType @ 0x556341168dc0> (None)
PLY: PARSE DEBUG END
===Finished Parsing===
```
As shown above, the scanner properly recognizes the input tokens existing in the
program given as an argument. It recognizes unspecified elements and has support
for comments. These tokens are then utilized by the parser to convert the
terminals into larger components of the program. The python package we used,
PLY, aka Python Lex-Yacc, utilizes LR parsing otherwise known as Shift-Reduce
parsing. This type of parsing takes the lower level components and builds up to
the higher level components, ie, a letter, assignment, and a number constant are
made into a variable, which is then a part of a variable declaration. LR parsing
specifically checks if the next token to the right is a valid addition to the
stack which can then be reduced using the grammar rules that have been specified
in the parser.

To test our scanner and parser we created a few sample programs that showed off
the main parts of Bosco's grammar and syntax. Here is a snippet of one of the
sample programs:
```
bone useLoop -treat z- (
  dig i = z| i < y| i = i + 1 (
    speak-"An Iteration!"|
    speak-i|
  )
)
```
The above snippet contains a function, a `speak` statement to print to the
terminal, and a `dig` loop which functions in a similar fashion to a Java for
loop.

## Conclusion
<!-- Conclusion. Give a short overview of your project and its results. Describe what you learned, what were the biggest challenges and the biggest rewards. -->

For our project, we set out to create a simple yet fun programming language
called Bosco. We were able to successfully create a grammar that included
dog-related elements (in honor of Bosco) and with this grammar, we were able to
construct sample programs to show how a regular Bosco program would look.
Creating the grammar was slightly challenging as we had to be creative and think
of how dog-related elements could be included in a way that made sense. After
this, we took steps to create a scanner and parser combination program that
would serve as a lexer and parser for the project's grammar. Unfortunately,
while our scanner functioned as intended right away, scanning in keywords and
tokens with no issue, our parser did not and took a lot of trial and error to
get it functional. This was undoubtedly the most challenging portion of the lab
because we ran into a number of errors that we could not fix when writing the
parser code and instead required us to change our grammar. Despite these
challenges, this project provided a variety of rewarding moments for our group.
For instance, it was very enjoyable to pursue the novel idea of creating a
programming language from scratch and being able to write programs in our
language after constructing our grammar. Additionally, it was also very
rewarding when we were able to get our scanner to work with our grammar and
especially when we finally got our parser working correctly after hours of
debugging. Ultimately, creating a working grammar, scanner, and parser were
rewarding moments and good learning experience for our group during the
completion of this project.
