# Silent JSON changes detector
[![example workflow](https://github.com/GautamGadipudi/tracky/actions/workflows/main.yml/badge.svg)](https://github.com/GautamGadipudi/tracky/actions/workflows/main.yml) [![Python 3.9.4](https://img.shields.io/badge/python-3.9.4-blue.svg)](https://www.python.org/downloads/release/python-394/)


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
 
#### 1. As a CLI:

```bash
# see usage and get help
python3 ./src/programs/program1.py --help
```

```bash
# collect mode
python3 ./src/programs/program1.py collect 
    --jsoninputpath <filename> 
    --outputdirectory <path>
    --verbose <boolean>
```

```bash
# match mode
python3 ./src/programs/program1.py match 
    --jsoninputpath <filename> 
    --targetfile <filename>
    --verbose <boolean>
```

Use `-v` or `--verbose` to enable verbose console logging

#### 2. Using built-in configurations (scenarios) in VSCode:
This approach is recommended when debugging.

```bash
# open cloned repository in VSCode
code .
```
> or just open the cloned repository in a new VSCode window 

    1. Open the "Run" tab in VSCode
    (shortcut - <kbd>shift</kbd> + <kbd>⌘</kbd> + <kbd>D</kbd>)

    2. Select a scenario to run from the "RUN" dropdown (typically on the top right corner)

    3. Click the green play button ("Start Debugging" button)

## Control flow
<div align="center"> <img src="./control_flow.jpeg" width="1200"></div>
