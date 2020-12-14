# Laplaces-s-Devil
Laplaces's Devil is a reflection loading framework

## Technical principle
Please visit my blog
https://idiotc4t.com/defense-evasion/reflectivedllinjection-variation
## How to usa
```bash 
python3 laplacessdevil.py -h

 _                 _                     _      ______           _ _
| |               | |                   ( )     |  _  \         (_) |
| |     __ _ _ __ | | __ _  ___ ___  ___|/ ___  | | | |_____   ___| |
| |    / _` | '_ \| |/ _` |/ __/ _ \/ __| / __| | | | / _ \ \ / / | |
| |___| (_| | |_) | | (_| | (_|  __/\__ \ \__ \ | |/ /  __/\ V /| | |
\_____/\__,_| .__/|_|\__,_|\___\___||___/ |___/ |___/ \___| \_/ |_|_|
            | |
            |_|

            Laplaces's Devil Is a reflection loading framework
                                v1.0 stable!
                    author idiotc4t@AtSec Lab!

usage: laplacessdevil.py [-h] [-m {addit,inject,patch}] [-f FILE]
                         [-n FUNCNAME] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -m {addit,inject,patch}, --method {addit,inject,patch}
                        PE file modification mode
  -f FILE, --file FILE  Input files to be processed
  -n FUNCNAME, --funcname FUNCNAME
                        The patch method requires additional function name
                        typing
  -o OUTPUT, --output OUTPUT
                        Output file name
```
## TODO
I haven't figured out what to do
[*]
## Credits
* stephenfewer ([@ReflectiveDLLInjection](https://github.com/stephenfewer/ReflectiveDLLInjection)) 
* hasherezade ([@pe_to_shellcode](https://github.com/hasherezade/pe_to_shellcode)) 
