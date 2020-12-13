import argparse
from core.patch import *
from core.inject import *
from core.addit import *

def logo():
     title = '''


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
    ''';
     print(title)

if __name__ == '__main__':
    logo()
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--method', type=str,choices=['addit', 'inject', 'patch'], default="addit", help='PE file modification mode')
    parser.add_argument('-f', '--file', type=str, default="", help='Input files to be processed')
    parser.add_argument('-n','--funcname', type=str, default="ReflectiveLoader", help='The patch method requires additional function name typing')
    parser.add_argument('-o', '--output', type=str, default="", help='Output file name')
    args = parser.parse_args()

    if args.file == "":
        parser.print_help()
        sys.exit()

    if args.method == 'addit':
        addit_pe(args.file,args.output)
    elif args.method == 'inject':
        inject_pe(args.file,args.output)
    elif args.method == 'patch':
        patch_dll(args.file,args.funcname,args.output)
    else:
        parser.print_help()


