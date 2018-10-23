# cmdline parser

Python command line program to parse BOM lines. Take-home code exercise for Tempo Automation

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

[Untar the file](https://www.pendrivelinux.com/how-to-open-a-tar-file-in-unix-or-linux/) -- How to untar.

Current version is written that it requires bomlines to be provided in a .txt file. This is despite reading the question prompt requesting reading purely from STDIN, seemingly as a consistent stream. That said, I have left a bom.txt file in the repo that already has example BOMS in it. 

You can run the parser program with the following syntax:

```python run.py 5 --bomfile bom.txt```

"5" in the above example represents N number of records we want to return. 

This run statement will output a JSON to STDOUT in the format requested. 

### Prerequisites

Python 3

## Running the tests

Explain how to run the automated tests for this system

There is a tests folder that contains two files. Either can be run manually with the following commands:

```
python tests/test_handle_part_input.py; 
python tests/test_parse.pypython tests/test_handle_part_input.py
```
The tests are not comprehensive or 1:1 based on the spec requirements. This is intentional. 

## Authors
Alex Tandy