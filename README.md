# The Bosco Programming Language

## Project Overview
This repository contains a work in progress programming language called `Bosco`.
Named after the lovable dog who roams around the home of the Allegheny College Department of Computer Science, Bosco is a simple programming language that draws
inspiration from languages such as Java, Python, and Decaf. Bosco contains many
dog-related elements and keywords, making it perfect for you or your super-
intelligent dog to use!

The project contains Bosco's grammar as well as a simple scanner and parser to
test Bosco programs with. Additionally, sample Bosco programs can be found in
the `src/samplePrograms` folder.

## Running The Scanner/Parser
To run the scanner/parser combo for the Bosco programming langauge, first ensure
Python3 is installed on your machine.

Finally, to run the scanner/parser while in the project's main directory, run the command below:
```
python3 src/parse_bosco.py FILENAME.bsco
```

### Example Run
First make sure Python3 is installed on your machine.

To run Bosco's scanner/parser while in the main directory with one of the
sample programs located in the `src/samplePrograms` directory, first follow the steps above.

For running the project with `basicSyntax.bsco` use the command:
```
python3 src/parse_bosco.py samplePrograms/basicSyntax.bsco
```

Or, to run the program while in the `src` folder with `basicSyntax.bsco`, simply use the command:
```
python3 parse_bosco.py samplePrograms/basicsyntax.bsco
```

## Project File Organization
- `docs` folder: Contains documents related to the project.
  sample programs.
  - `writing` folder: Contains the writing for the project. Interested users can read more into the thought process about Bosco and find out about more of its attributes by reading these documents.
  - `sampleOutput` folder: Contains the output from the scanner/parser for the test programs.
- `src` folder: Houses the code for the scanner/parser in the file `parse_bosco.py`
  - `samplePrograms` folder: Contains sample/test Bosco programs.

## Ideas or Issues?
Please make an issue in the project's GitHub Issue Tracker.

There is no guarantee that this project will be updated again.

## Contributors
Thanks to those who contributed to this project:
  - Christian Lussier ([See GitHub Profile](https://github.com/lussierc))
  - Zach Andrews ([See GitHub Profile](https://github.com/ZachAndrews98))
  - Devin Spitalny ([See GitHub Profile](https://github.com/spitalnyd))
