# Tracking COVID-19 numbers from Command Line/TouchBar
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
## Screenshots
Used in terminal
![alt text](https://github.com/tienbach/COVID-19-tracker/raw/master/screenshot.png "Terminal")

Used on TouchBar
![alt text](https://github.com/tienbach/COVID-19-tracker/raw/master/touchbarshot.png "TouchBar")

## TouchBar Widget
If you want even more depression looking at the case numbers:
- Install [BetterTouchTool](https://folivora.ai/) and open it
- Choose `Touch Bar` in the dropdown menu on top and then the plus `+` sign at the bottom
- In the `Touch Bar Trigger Config` column, choose `Shell Script / Task Widget`
- In the `Scipt` field, put `echo $(python3 [Path to tracker_touchbar.py] -a us germany)` to track active cases for the US and Germany. Optional args: `-a` active cases, `-d` deaths, `-r` recovered cases. Active cases number shown by default
- In the `Execute script every` field, put what you want. For me it's `3600`
- If you use virtualenv, make sure to put the command to activate it before the command above

## Notes
- `termgraph.py` is copied over from `https://github.com/mkaz/termgraph` with 2 lines of bug fix of mine
- Tested only on macOS Catalina with Python 3.7
