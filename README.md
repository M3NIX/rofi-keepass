# rofi-keepass

A rofi frontend to quickly access your keepass file

## Installing

`pip install -r requirements.txt --user`

Following packages are needded:

- xdotool
- xclip

## Usage

Create a keybinding which launches the script like...

`python rofi-keepass.py --database /path/to/your/keepass.kdbx`


# Keyboard shortcuts

|  Shortcut |     Action    |
|:---------:|:-------------:|
|  Enter    |   Copy password to clipboard    |
|  Alt+1    |   Type All    |
|  Alt+2    |   Type User   |
|  Alt+3    | Type Password |  
