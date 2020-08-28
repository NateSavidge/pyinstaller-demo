# Setup
- Commands below were tested in the MacOS terminal.
- `pip install pyinstaller numpy`
- Check that the python script is working with: `python script.py 5` (5 is the argument for the "range" input)
- The output should be the array `[[0 1][2 3][4 5][6 7][8 9]]`

# Create the executable app:
- `pyinstaller --onefile script.py`
- An Generates an executable named `script` in a folder named `/dist` 
- This can be run in a shell from the root directory with the command `dist/script`