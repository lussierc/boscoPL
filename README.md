# cs401s2019-project README
### Group Members: Zach Andrews, Christian Lussier, Devin Spitalny

## Project Overview
This repository contains a work in progress programming language called `Bosco`.
Named after the lovable dog who roams around the home of the Allegheny College
Computer Science Department, Bosco is a simple programming language that draws
inspiration from languages such as Java, Python, and Decaf. Bosco contains many
dog-related elements and keywords, making it perfect for you or your super-intelligent
dog to use!

The project contains Bosco's grammar as well as a simple scanner and parser to
test Bosco programs with. Additionally, sample Bosco programs can be found in
the `test` folder.

## Running The Scanner/Parser
To run the scanner/parser combo for the Bosco programming langauge, first ensure
Python3 is installed on your machine.

Finally, to run the scanner/parser, run the command below:
```
python3 src/parse_bosco.py test/FILENAME.bsco
```

### Example Run
To run Bosco's scanner/parser with one of the sample programs located in the `test`
directory, first follow the steps above.

For running the project with `basicSyntax.bsco` use the command:
```
python3 src/parse_bosco.py test/sampleprog1.bsco
```

## Project File Organization
- `output` folder: Contains output from running the scanner/parser with Bosco's
  sample programs.
- `src` folder: Houses the code for the scanner/parser in the file `parse_bosco.py`
- `test` folder: Contains sample/test Bosco programs.
- `writing` folder: Contains the writing for the project. Interested users can
  read more into the thought process about Bosco and find out about more of it's
  attributes by reading these documents.
