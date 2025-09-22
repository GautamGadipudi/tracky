# Silent JSON changes detector
[![example workflow](https://github.com/GautamGadipudi/tracky/actions/workflows/main.yml/badge.svg)](https://github.com/GautamGadipudi/tracky/actions/workflows/main.yml) [![Python 3.9.4](https://img.shields.io/badge/python-3.9.4-blue.svg)](https://www.python.org/downloads/release/python-394/) [![RIT-CS](https://img.shields.io/badge/RIT-CS-orange.svg)](https://www.rit.edu/study/computer-science-ms)

In this capstone project, we implement a static class in Python3 with static methods to capture details about the operations - frame metadata - performed on JSON data, log this frame metadata, and match it against target frame metadata to discover examples and scenarios of silent JSON errors in Python3 programs. 

## Getting the code
Run either of the below commands in the terminal:
```bash
# for https connections
git clone https://github.com/GautamGadipudi/tracky.git

# for ssh connections
git clone git@github.com:GautamGadipudi/tracky.git
```

## Installation

#### Requirements:
1. [![Python 3.9.4](https://img.shields.io/badge/python-3.9.4-blue.svg)](https://www.python.org/downloads/release/python-394/)

#### Install dependencies:
```bash
cd tracky

python -m pip install --upgrade pip
pip install -r requirements.txt
```

``` bash
# Make sure you have modules accessible to the interpretter
export PYTHONPATH="$PYTHONPATH:<your-relative-path-to-repo>/src"
```
## Running the code

---

All programs are located in `./src/programs/`

---
 
#### 1. As a CLI:
```bash
# see usage and get help
python3 <path-to-a-program> --help
```

```bash
# collect mode
python3 <path-to-a-program> collect 
    --jsoninputpath <filename> 
    --outputdirectory <path>
```

```bash
# match mode
python3 <path-to-a-program> match 
    --jsoninputpath <filename> 
    --targetfile <filename>
```

<sup>Use `-v` or `--verbose` to enable verbose console logging</sup>

#### 2. Using built-in configurations (scenarios) in VSCode:
This approach is recommended when debugging.

```bash
# open cloned repository in VSCode
code .
```

<sup>or just open the cloned repository in a new VSCode window </sup>

<ol>
  <li>Open the "Run" tab in VSCode (shortcut - <kbd>shift</kbd> + <kbd>⌘</kbd> + <kbd>D</kbd>)</li>
  <li>Select a scenario to run from the "RUN" dropdown (typically on the top right corner)</li>
  <li>Click the green play button ("Start Debugging" button)</li>
</ol>

#### 3. Run all programs (both collect and match), for all overloaded methods, for all examples
```bash
python3 ./src/tests/run_all.py
```

## Control flow
<div align="center"> <img src="./control_flow.jpeg" width="1200"></div>

## Poster
<div align="center"> <img src="./poster.jpg" width="1200"></div>
