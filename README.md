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
- Then you can set an alias like `alias covid="python COVID-19-tracker/tracker.py"` to quickly track numbers

## Examples
```
python tracker.py
python tracker.py us
python tracker.py us germany netherlands
```

## TouchBar Widget
If you want even more depression looking at the case numbers:
- Install [BetterTouchTool](https://folivora.ai/) and open it
- Choose `Touch Bar` in the dropdown menu on top and then the plus `+` sign at the bottom
- In the `Touch Bar Trigger Config` column, choose `Shell Script / Task Widget`
- In the `Scipt` field, put `echo $(python3 \[Path to tracker_touchbar.py\] us germany)` to track numbers for US and Germany. Of course feel free to change the countries as you want
- In the `Executr script every`, put what you want. For me it's `3600`
- If you use virtualenv, make sure to put the command to activate it before the command above
- Right now it only supports showing number of active cases...

## Notes
- `termgraph.py` is copied over from `https://github.com/mkaz/termgraph` with 2 lines of bug fix of mine
- Tested only on macOS Catalina with Python 3.7
