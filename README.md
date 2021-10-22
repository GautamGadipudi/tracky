# Silent JSON changes detector
![example workflow](https://github.com/GautamGadipudi/tracky/actions/workflows/main.yml/badge.svg)

## Clone the repo.
```
git clone https://github.com/GautamGadipudi/tracky.git
```

## Run different configurations (scenarios) in VSCode debugger
Open the `Run` tab in VSCode (shortcut - `shift` `⌘` `D`)

## CLI to run tracky in different modes
Make sure you have modules accessible to the interpretter
```
export PYTHONPATH="$PYTHONPATH:./src"
```

Use the below command to get help on how to use the CLI
```
python3 ./src/programs/program1.py --help
```

### Collect mode
```
python3 ./src/programs/program1.py collect --jsoninputpath <filepath>
```
### Match mode
```
python3 ./src/programs/program1.py match --jsoninputpath <filepath> --targetfile <filepath>
```

> Use `--verbose` or `-v` to see frame details