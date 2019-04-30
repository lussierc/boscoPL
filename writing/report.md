# CS401 Project Report
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

There actually are already dog-inspired programming languages that are publicly availably. However, until the week before the report was due, we had no idea that a dog-related toy programming language existed. Despite this, there is a language called ["DOG"](https://esolangs.org/wiki/DOG) which is very much dog-related. Created by Jeremy Ruten, the programs for this language use commands that are supposed to look like commands that you would give to a dog. For instance, "fetch" is used to add, "drop" is used to subtract, and "bark" is used to print. It is extremely simple, with no real mainstream formatting, unlike that which appears in Java such as the use of brackets ({}) to denote where the body of methods and classes appear.

As mentioned earlier, one other fun-motivated programming language is Trump Script. Trump Script is based on Donald Trump phrases and speaking habits. While it is not super-functional by any means, it is quite interesting and fun if you follow American politics. In this sense it was a motivation for our program, as it strived to create a fun and real-world relevant programming language.

### References:
- "DOG" Programming Language: https://esolangs.org/wiki/DOG
- Trump Script: https://github.com/samshadwell/TrumpScript
## Overview of Completed Work
<!-- Detailed description of the work you completed for this project. Without giving a snap- shot of the code you wrote, describe what you implemented and how you implemented it. -->
## Overview of Results
 <!-- Description of your results. Make graphs, tables, snapshot of output, or anything else that can help me understand your results. -->
## Conclusion
<!-- Conclusion. Give a short overview of your project and its results. Describe what you learned, what were the biggest challenges and the biggest rewards. -->

Grammar:
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
