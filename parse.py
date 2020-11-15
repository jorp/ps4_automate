#!/usr/bin/env python3
import os
import re
import sys

cmd_dict = {
        "jshort":"xdotool_key",
        "c":"0xff08",
        "t":"0x0043",
        "x":"0xff0d",
        "s":"0x005c",
        "dr":"0x08fd",
        "dd":"0x08fe",
        "dl":"0x08fb",
        "du":"0x08fc",
        "r1":"0x0033",
        "r2":"0x0034",
        "r3":"0x0036",
        "l1":"0x0032",
        "l2":"0x0031",
        "l3":"0x0035",
        "ll":"0x005b",
        "ld":"0xffff",
        "lr":"0x005d",
        "lu":"0xff63",
        "rl":"0x002d",
        "rd":"0xff56",
        "rr":"0x003d",
        "ru":"0xff55",
        "sh":"0x0046",
        "ps":"0xff1b",
        "op":"0x004f",
        "tp":"0x0054"
        }

commands = []
def look_up_keycode(key):
    return keycode
def run_commands(button, repeat = "1"):
    print("xdotool key --repeat {} --delay 1000 '{}'".format(repeat, button))

with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        match = re.match(r"([0-9]+)([a-z]+)", line, re.I)
        if match:
            items = match.groups()
            #print(items)
            commands.append(items)
        else:
            #print(line.strip())
            commands.append(line.strip())

#print(commands)
for item in commands:
    if type(item) is tuple:
        repeat = item[0]
        cmd = item[1]
        run_commands(cmd, repeat)
    else:
        run_commands(item)

