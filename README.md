# Tracking COVID-19 numbers from command line
- Summary of COVID-19 cases globally and for specific countries
- Bar graphs of historical numbers of cases

## Usage
- Clone this repo `git clone https://github.com/tienbach/COVID-19-tracker.git`
- Install modules in requirements `pip install -r requirements.txt`
- Run:
```
python COVID-19-tracker/tracker.py [country ...]
```

## Examples
```
python tracker.py
python tracker.py us
python tracker.py us germany netherlands
```

## Roadmap
- Input number of days drawn on graph
- ...

## Note
- `termgraph.py` is copied over from `https://github.com/mkaz/termgraph` with 2 lines of bug fix of mine.
- Tested only on macOS Catalina
