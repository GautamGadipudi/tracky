# Silent JSON changes detector

## Clone the repo.
```
git clone https://github.com/GautamGadipudi/tracky.git
```

## Run different configurations (scenarios) in VSCode debugger
Open the `Run` tab in VSCode (shortcut - `shift` `⌘` `D`)

## Commands
### Mode `collect`
```
python3 detector.py collect --jsoninputpath <filepath>
```
### Mode `match`
```
python3 detector.py match --evaluationfile <filepath> --targetfile <filepath>
```