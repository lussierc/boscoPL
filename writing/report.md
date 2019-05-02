# CS401 Project - Final Report
### Zachary Andrews, Devin Spitalny, Christian Lussier

## Introduction
For our CS401 Final Project, we decided to create a toy programming language, much like the ones discussed in class. When coming up with a name for our simple language, our minds immediately jumped to the lovable dog and unofficial Allegheny Computer Science mascot, Bosco. With this in mind we set about creating our new Bosco programming language, drawing inspiration from other languages such as Java and Python as well as toy languages such as Decaf and C0. We created a basic grammar for our language with dog-related elements, including dog phrases like "woof" and "bone" to add a dog flair of sorts. Additionally, we also took steps to create a simple scanner/parser for our language. When creating Bosco, we tried to create a fun and easy to understand grammar that would work well with our scanner and parser.

## Project Motivation
<!-- The motivation for your project. Why is the problem you decided to solve important/useful? -->
When deciding on what to create for our compiler-related CS401 final project, there were a number of motivating factors involved. While in class one day, Professor Jumadinova mentioned the idea of making a programming language for our final project, as it would be compiler-related. Our group was a little tentative on this at first, but we were motivated to pursue this idea because creating our own programming language sounded like a really cool idea. Once we had decided to create a programming language, we were also motivated to make a fun and simple language. Eventually we came up with the idea of naming it Bosco and from there, making a programming language with dog-related elements provided the fun portion of motivation that we were looking for.

Additionally, once we had decided to make a toy or mini programming language, we were motivated by many of the toy-programming languages that already existed. "Trump Script" probably motivated us the most in this regard, because it was a fun and playful programming language, based on many of Donald Trump's speaking habits, that kind of exemplified what we wanted our programming language to be in a way (except ours is dog-related instead of Trump-related). We were also motivated by the mini-programming languages that students were using for their compiler labs in class. The one that influenced and motivated us the most was likely Decaf, because we found it cool that it was basically a mini programming language for Java and C#. Additionally, all of the project's group members had used Decaf for their compilers.

## Background Information
<!-- Background for the proposed problem. What have others done for it a lready? Include references. -->
While our programming language doesn't solve a specific, real-world applicable problem, it is an attempt to solve the problem of a lack of fun elements existing in many programming languages. Our group feels that in most mainstream languages, there just aren't many fun elements though this makes sense because these languages are being used for real-world work. Many people seem to feel similarly, as many toy programming languages have been created in recent years.

There actually are already dog-inspired programming languages that are publicly available. However, until the week before the report was due, we had no idea that a dog-related toy programming language existed. Despite this, there is a language called ["DOG"](https://esolangs.org/wiki/DOG) which is very much dog-related. Created by Jeremy Ruten, the programs for this language use commands that are supposed to look like commands that you would give to a dog. For instance, "fetch" is used to add, "drop" is used to subtract, and "bark" is used to print. It is extremely simple, with no real mainstream formatting, unlike that which appears in Java such as the use of brackets ({}) to denote where the body of methods and classes appear.

As mentioned earlier, one other fun-inspired programming language is Trump Script. Trump Script is based on Donald Trump phrases and speaking habits. While it is not super-functional by any means, it is quite interesting and fun if you follow American politics. In this sense it was a motivation for our program, as it strived to create a fun and real-world relevant programming language.

### References:
- "DOG" Programming Language: https://esolangs.org/wiki/DOG
- Trump Script: https://github.com/samshadwell/TrumpScript

## Overview of Completed Work
<!-- Detailed description of the work you completed for this project. Without giving a snap- shot of the code you wrote, describe what you implemented and how you implemented it. -->
Once we finalized the idea for our project, we completed work in a variety of different areas. The first of these areas was creating a grammar for our project. We took the time to create a grammar (that Bosco himself would love) that contained a lot of whimsical dog-related elements. For example, our reserved keywords included `woof`, `bone`, `speak`, `dig`, `int`, `double`, `fetch`, and more. For instance, `woof` will be used for classes, `bone` will be used for functions, `speak` will be used to print things to the terminal, and `dig` will be used as a simple loop (like a for loop). These keywords will play a large role in program structure and functionality.

Once we completed creating our grammar, we wrote a sample program for the Bosco language to get a general idea of how it would function. This first sample program, entitled `sampleprog1` included loops, functions, and variable declarations. With this it included some simple mathematical operations on these variables and `speak` statements to print output to the terminal.

After finalizing our grammar and writing a sample program, we began the implementation portion of our project. This involved implementing a scanner and parser for our new Bosco language to use with our created sample programs. To start, we began by

## Overview of Results
 <!-- Description of your results. Make graphs, tables, snapshot of output, or anything else that can help me understand your results. -->

While completing this project and completing a variety of work, we produced a variety of mixed results. The first of these was the successful creation of a grammar with dog-related elements.

The Bosco Grammar:
```
Program ::== Decl+
Decl ::= BoneDecl | WoofDecl | VarDecl
WoofDecl ::= woof ID: Field* :
BoneDecl ::= bone ID- Formals: StmtBlock
Var ::= Type ID
VarDecl ::= Var\|
StmtBlock ::= : VarDecl* Stmt* :
Stmt ::= 〈Expr〉 \| | IfStmt | DigStmt | BreakStmt | ReturnStmt | SpeakStmt | StmtBlock
Field ::= VarDecl | FuncDecl
Formals ::= Variable+, | ε
SpeakStmt ::= Speak- Expr+, \|
IfStmt ::= if ( Expr ) Stmt 〈else Stmt〉
ReturnStmt ::= return〈Expr〉\|
BreakStmt ::= break\|
DigStmt ::= dig- Type ID Expr| Expr | Expr: Stmt
Expr ::= LValue = Expr | Constant | LValue | this | ( Expr ) | Expr+Expr | Expr-Expr | Expr*Expr | Expr/Expr | Expr%Expr | - Expr | Expr < Expr | Expr <= Expr | Expr > Expr | Expr >= Expr | Expr == Expr | Expr != Expr | Expr && Expr | Expr || Expr | ! Expr | FetchInteger ( ) | FetchLine ( )
LValue ::= indent (Actuals) | Expr . indent (Actuals)
Actuals ::= Expr+, | ε
Type ::= int | double | bool | string
Constant ::= intConstant | doubleConstant | boolConstant | stringConstant | null
```

After creating our grammar, we worked to create a scanner and parser utilizing it. The result for this task did not end as successfully as we wished. We created a working scanner and a semi-working parser, but we could just not figure out how to fix some of the issues the parser was encountering. This was by far the most challenging part of the project as we ran into a variety of issues while trying to get our scanner and parser to work.

Here is the current output from running the scanner/parser combination on `sampleprog1.bsco`:
```
LexToken(WOOF,'woof',2,42)
LexToken(ID,'classBosco',2,47)
LexToken(COLON,':',2,57)
LexToken(BONE,'bone',3,61)
LexToken(ID,'myFunction',3,66)
LexToken(MINUS,'-',3,76)
LexToken(COLON,':',3,77)
LexToken(INT,'int',4,83)
LexToken(ID,'x',4,87)
LexToken(ASSIGN,'=',4,89)
LexToken(INT,'2',4,91)
LexToken(BAR,'|',4,92)
LexToken(INT,'int',5,98)
LexToken(ID,'y',5,102)
LexToken(ASSIGN,'=',5,104)
LexToken(INT,'17',5,106)
LexToken(BAR,'|',5,108)
LexToken(INT,'int',6,114)
LexToken(ID,'z',6,118)
LexToken(ASSIGN,'=',6,120)
LexToken(ID,'x',6,122)
LexToken(PLUS,'+',6,124)
LexToken(ID,'y',6,126)
LexToken(BAR,'|',6,127)
LexToken(SPEAK,'speak',7,133)
LexToken(MINUS,'-',7,138)
LexToken(ID,'z',7,139)
LexToken(BAR,'|',7,140)
LexToken(COLON,':',8,190)
LexToken(BONE,'bone',9,194)
LexToken(ID,'myOtherFunction',9,199)
LexToken(MINUS,'-',9,214)
LexToken(COLON,':',9,215)
LexToken(SPEAK,'speak',10,221)
LexToken(MINUS,'-',10,226)
LexToken(STRING,'"I am Bosco. I am speaking woof woof."',10,227)
LexToken(BAR,'|',10,265)
LexToken(DIG,'dig',11,271)
LexToken(MINUS,'-',11,274)
LexToken(ID,'i',11,275)
LexToken(ASSIGN,'=',11,277)
LexToken(INT,'0',11,279)
LexToken(BAR,'|',11,280)
LexToken(ID,'i',11,282)
LexToken(LESS,'<',11,284)
LexToken(INT,'10',11,286)
LexToken(BAR,'|',11,288)
LexToken(ID,'i',11,290)
LexToken(PLUS,'+',11,291)
LexToken(PLUS,'+',11,292)
LexToken(COLON,':',11,293)
LexToken(SPEAK,'speak',12,301)
LexToken(MINUS,'-',12,306)
LexToken(ID,'i',12,307)
LexToken(BAR,'|',12,308)
LexToken(COLON,':',13,314)
LexToken(COLON,':',14,318)
LexToken(ID,'myOtherFunction',15,322)
LexToken(MINUS,'-',15,337)
LexToken(BAR,'|',15,338)
LexToken(COLON,':',16,368)
Syntax error in input
Syntax error in input
```
As shown above, the scanner properly recognizes the input tokens existing in the program given as an argument. However, the bottom two lines of the program are where the issues with our parser begin. When completing debugging tasks these issues become more detailed and specific, but despite this it was hard to figure out exactly what was causing the parser to fail. Even with every group member looking through the source code multiple times and using a variety of testing methods, we were unable to find the bug. This resulted in the production of only a partially working scanner and parser combination program, with the scanner being seemingly functional and the parser encountering issues that were detrimental to its functionality.

To test our scanner and parser we created a few sample programs that showed off the main parts of Bosco's grammar and syntax. Here is a snippet of one of the sample programs:
```
bone myOtherFunction-:
  speak-"I am Bosco. I am speaking woof woof."|
  dig-i = 0| i < 10| i++:
    speak-i|
  :
:
myOtherFunction-| ?? I am calling my function
```
The above snippet contains a function, a `speak` statement to print to the terminal, and a `dig` loop which functions in a similar fashion to a Java for loop. Additionally, there is an example of the function being called.

## Conclusion
<!-- Conclusion. Give a short overview of your project and its results. Describe what you learned, what were the biggest challenges and the biggest rewards. -->

For our project we set out to create a simple yet fun programming language called Bosco. We were able to successfully create a grammar that included dog-related elements (in honor of Bosco) and with this grammar we were able to construct sample programs to show how a regular Bosco program would look. Creating the grammar was slightly challenging as we had to be creative and think of how dog-esque elements could be included in a way that made sense. After this, we took steps to create a scanner and parser combination program that would serve as a lexer and parser for the project's grammar. Unfortunately, while our scanner functioned as intended, scanning in keywords and tokens with no issue, our parser did not. This was undoubtedly the most challenging portion of the lab because we ran into an number of errors that we could not fix when writing the parser code. Despite each group member spending hours to try and fix these issues, we simply could not figure out what was causing the parser to fail. Despite these failure-inducing challenges, this project provided a variety of rewarding moments to our group. For instance, it was very enjoyable to pursue the novel idea of creating a programming language from scratch and being able to write programs in our language after constructing our grammar. Additionally, it was also very rewarding when we were able to get our scanner to work with our grammar. While our Bosco programming language's parser did not end up working, creating a grammar and scanner were rewarding moments and good learning experience for our group during the completion of this project. 
