# bomdotcom parser

Python command line program to parse BOM lines. Take-home code exercise for Tempo Automation

## Getting Started

[Untar the project folder](https://www.pendrivelinux.com/how-to-open-a-tar-file-in-unix-or-linux/) -- How to untar.

Current version is written such that it requires bomlines to be provided in a .txt file. This is despite reading the question prompt requesting reading from STDIN. That said, I have left a bom.txt file in the repo that already has example Parts in it. 

You can run the parser program with the following syntax:

```python run.py 5 --bomfile bom.txt```

"5" in the above example represents N number of records we want to return. 

This run statement will output JSON to STDOUT in the format requested. 

### Prerequisites

Python 3

## Running the tests

There is a tests folder that contains a single file. It can be run manually with the following command:

```
python tests/test_parse.py
```

The tests are not fully comprehensive or 1:1 based on the spec requirements. This is intentional. 

## Authors
Alex Tandy