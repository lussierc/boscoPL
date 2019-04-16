# Progress Report - Bosco Programming Language

### Zachary Andrews, Devin Spitalny, Christian Lussier
### April 16, 2019

## Introduction

For our project, we decided to create "Bosco", a mini-programming language grammar complete with a scanner and parser. It will be a novelty programming language with a functional and simplistic syntax for its users, making it both fun and useful. Since coming up with our project idea we have completed a variety of tasks. We came up with some simple keywords and grammar to help us get started. We then created a sample program that will serve as a good basis for our language and also as a test program for our scanner and parser. Despite this, we have also faced challenges like getting our scanner/parser to work, coming up with a grammar, and more. Over the last couple of weeks, we have begun to come up with ideas for our programming language grammar and it's scanner.

## Progress

After our project was approved by Professor Jumadinova, we first came up with some ideas to include in our language. For instance, we decided our programming language needed to include functions, data types (like integers, strings, and booleans), if/if else/else functionality, and loops. Additionally, we also saw the need for language library functions (like printing and input gathering from the terminal) and comments. After this, we were able to proceed with coming up with reserved keywords and a simple grammar for our language.

Our reserved keywords include:
```
woof, bone, speak, dig, int, double, fetch
```

Though there are more reserved keywords, all of these will be useful for our programming language. For example, `woof` will be used for classes, `bone` will be used for functions, `speak` will be used to print things to the terminal, and `dig` will be used as a simple loop (like a for loop). These keywords will play a large role in program structure and functionality.

After determining our reserved keywords, we came up with a sample program to get a general idea of what our languages programs would like. This sample program can be found in `src/sampleprograms/sampleprog1.bsco`. This sample program should be useful for testing our scanner/parser when it is complete. Additionally, this sample program will be good to look at to refresh our memories on the grammar we created and get a general idea of how a program will be structured in the Bosco programming language.

Here is part of the Bosco sample program, that gives a general idea of the programming language's structure, in its current state:
```
woof classBosco:
  bone myFunction-:
    int x = 2|
    int y = 17|
    int z = x + y|
    speak-z|  ?? This is my comment. Here we are printing.
  :
```

After coming up with a basic grammar and a sample program for our new mini-programming language, we began to work on a scanner and parser to work with this language. Currently, we have implemented support for most of our reserved keywords in this scanner/parser combination. Also, we have begun to add tokens that will be used for operations and organizations of code in a Bosco program. Our scanner/parser currently has limited functionality, recognizing many of the reserved keywords and tokens that we have defined. Additionally, it also recognizes undefined characters such as a `.`. Overall, there is more work to be done on our scanner/parser and we have faced some challenges in implementing it, some of which are detailed below.

Here is some of our scanner's current output when tested with the above sample program:
```
LexToken(ID,'Bosco',1,3)
LexToken(ID,'Language',1,9)
LexToken(MINUS,'-',1,18)
LexToken(ID,'First',1,20)
LexToken(ID,'Sample',1,26)
LexToken(ID,'Program',1,33)
Illegal character '.'
LexToken(WOOF,'woof',3,43)
LexToken(ID,'classBosco',3,48)
LexToken(COLON,':',3,58)
LexToken(BONE,'bone',4,62)
LexToken(ID,'myFunction',4,67)
LexToken(MINUS,'-',4,77)
LexToken(COLON,':',4,78)
```

# Challenges

Some challenges we have come up so far in this project included was figuring out what fully we were going to do with our project. The whole idea was to make another language but at first, we struggled with coming up with an idea that the language could be based on till we saw Bosco the dog come out of one the classrooms with Professor Kapfhammer. That's when we solved our first challenge of finding what our programming language would be about as we decided to make a unique language for dogs honored by Bosco. The next challenge was coming up with grammar to put in our dog-based mini-programming language. We solved this issue by searching dog commands for fun. That gave us the idea to use those commands we found on the internet as grammar that will replace common grammar from common languages like java and python. So, as mentioned earlier, for example, we use terms like woof to represent the class, bone represents a function, speak represents print statements, and dig represent loops. We just use those terms to represent the original meanings of other languages so we can make this language sound like a dog would understand everything going on.

The next challenge we are having is the hardest one yet. We haven't figured how to completed solve this challenge yet and it is all about using the grammar we implemented and getting the scanner/parser to work with our newly created grammar. Right now, due to some parts of the scanner/parser being incomplete, it recognizes some parts of our sample program as invalid or it recognizes them as tokens that they actually aren't. Some ways we might be able to solve this problem is just maybe starting over or going through the lines of code in our scanner to see what mistakes we have made and what we need to add in order to create a fully functional scanner/parser for our language.

## Conclusion

Though we have completed a lot of work on this project, there is still more to be done. Some of the main things that have been completed up to this point include the creation of a simple grammar with reserved keywords for the Bosco programming language and a simple sample program that gives a general idea of the program structure. This was somewhat challenging as we wanted the make the language both fun (as if it was written by a dog) and functional. After this, we began to work on our scanner/parser program combination. It has some limited functionality at this time, scanning in some of our reserved keywords and recognizing some invalid syntax. Despite this, more work needs to occur for this scanner/parser to fully work with Bosco. Overall, we have made some good progress on this project and despite running into some challenges, we have a partially completed scanner/parser for our work-in-progress mini-programming language.
