# ps4_automate

full write-up available on my blog [here](https://jorp.xyz/posts/ps4-automate/).

## requirements

- [Chiaki](https://github.com/thestr4ng3r/chiaki)
- [xdotool](https://www.semicomplete.com/projects/xdotool)
- [wmctrl](http://tripie.sweb.cz/utils/wmctrl)
- [Python3](https://www.python.org)
- Distro/DE using an Xorg Session

## usage
```bash
$ python ps4_automate.py <macro input file>
```

### Example
The included `example.txt` would map to the following:
```text
3lu		--> 3x left-stick up
rl		--> 1x right-stick left
rr		--> 1x right-stick right
rr		--> 1x right-stick right
rl		--> 1x right-stick left
2t		--> 2x triange
r2		--> 1x R2
```

### Keymap table

| ps4_button        | chiaki_default    | xdotool_key_code | button_shorthand |
|-------------------|-----------|-------------|--------|
| Circle            | Backspace | 0xff08      | c      |
| Triangle          | C         | 0x0043      | t      |
| X                 | Return    | 0xff0d      | x      |
| Square            | \         | 0x005c      | s      |
| D-Pad Right       | Right     | 0x08fd      | dr     |
| D-Pad Down        | Down      | 0x08fe      | dd     |
| D-Pad Left        | Left      | 0x08fb      | dl     |
| D-Pad Up          | Up        | 0x08fc      | du     |
| R1                | 3         | 0x0033      | r1     |
| R2                | 4         | 0x0034      | r2     |
| R3                | 6         | 0x0036      | r3     |
| L1                | 2         | 0x0032      | l1     |
| L2                | 1         | 0x0031      | l2     |
| L3                | 5         | 0x0035      | l3     |
| Left Stick Left   | [         | 0x005b      | ll     |
| Left Stick Down   | Del       | 0xffff      | ld     |
| Left Stick Right  | ]         | 0x005d      | lr     |
| Left Stick Up     | Ins       | 0xff63      | lu     |
| Right Stick Left  | -         | 0x002d      | rl     |
| Right Stick Down  | Page_Down | 0xff56      | rd     |
| Right Stick Right | =         | 0x003d      | rr     |
| Right Stick Up    | Page_Up   | 0xff55      | ru     |
| Share             | F         | 0x0046      | sh     |
| PS                | Esc       | 0xff1b      | ps     |
| Options           | O         | 0x004f      | op     |
| Touchpad          | T         | 0x0054      | tp     |
