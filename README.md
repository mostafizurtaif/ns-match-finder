# NS-Match-Finder
NS-Match-Finder is short for Number-Sequence-Match-Finder. This project contains two files ―

1. ```ns_tmatch.py```
2. ```sanitize.py```

The latter is a module used in the former file.

# Usage
It takes a ```.txt``` file containing number sequence, not necessarily formatted correctly (```sanitize.py``` has a ```sanitize_ns``` function that can sanitize number sequence), and then reads it. It prompts the user to give it a number sequence, and it runs the number sequence in the former one and checks if there is a match. And it finally returns the total hits.

# Prerequisites
You must have already installed [Python 3](https://www.python.org/downloads/) on your local computer.

# How to Use
Just run the ```ns_tmatch.py``` like another python file.
