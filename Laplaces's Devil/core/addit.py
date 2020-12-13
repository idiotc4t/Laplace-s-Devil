import sys
import pefile
from struct import pack
from core.lib import *
from core.inject import get_inject_bootstrap

def addit_help():
    print("usage: python3 <PePath>")
    sys.exit()


def addit_pe(pe_path,out_name):
    pe_file = get_pe_load(pe_path)

    pe_file_array = open(pe_path, 'rb').read()
    print("[+] loaded nameof %s" % (pe_path))

    addit_bootstrap = get_inject_bootstrap(pe_file,len(pe_file_array))

    if get_pe_bit(pe_file):
        addit_stub = open('resources/stub64.bin', 'rb').read()
    else:
        addit_stub = open('resources/stub32.bin', 'rb').read()

    addit_pe_file = addit_bootstrap + pe_file_array[len(addit_bootstrap):] + addit_stub
    print("[+] patched offset %d" % (len(pe_file_array)))

    write_pe_file(addit_pe_file, pe_path, out_name)



