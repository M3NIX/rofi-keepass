#!/usr/bin/env python3

from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsIntegrityError
import subprocess
import argparse
import shlex
import os

from notify import Notification
from rofi import Rofi

# initialize argument parser
parser = argparse.ArgumentParser(description='Rofi frontend for keepassxc interaction')
parser.add_argument('--database', help='Path to your keepass database', required=True)
args = parser.parse_args()

# initialize rofi
r = Rofi()
password = r.text_entry('Master Password', rofi_args=['-password', '-lines', '0'])

try:
    # load database
    kp = PyKeePass(args.database, password=password)
except CredentialsIntegrityError as e:
    r.exit_with_error('Could not open database')

options = []
for entry in kp.entries:
    options.append(entry.title)

index, key = r.select('Name', options, key1=('Alt+1', "Type all"), key2=('Alt+2', "Type user"), key3=('Alt+3', "Type pass"), rofi_args=['-i', '-no-custom'])

if(key == 0):
    # copy password
    cmd = "echo -n '" + shlex.quote(kp.entries[index].password) + "' | xclip -selection clipboard"
    subprocess.Popen(cmd,shell=True).communicate()
    Notification("Will be cleared in 15 seconds", kp.entries[index].title + " copied")
    subprocess.Popen("sleep 15 && echo -n "" | xclip -selection clipboard -r", shell=True).communicate()
elif(key == 1):
    # type all
    subprocess.call(["xdotool", "type",  kp.entries[index].username])
    subprocess.call(["xdotool", "key",  "Tab"])
    subprocess.call(["xdotool", "type",  kp.entries[index].password])
elif(key == 2):
    # type user
    subprocess.call(["xdotool", "type",  kp.entries[index].username])
elif(key == 3):
    # type password
    subprocess.call(["xdotool", "type",  kp.entries[index].password])
