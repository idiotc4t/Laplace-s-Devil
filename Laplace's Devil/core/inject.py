import sys
import pefile
from struct import pack
from core.lib import *

def inject_help():
    print("usage: python3 <PePath>")
    sys.exit()



def get_inject_bootstrap(pe_file,func_offset):

    bootstrap = (
        b"\x4d"+
		b"\x5A" +#pop edx
		b"\x45" +#inc ebp
		b"\x52" +#push edx
		b"\xE8\x00\x00\x00\x00" +#call <next_line>
		b"\x5B" +# pop ebx
		b"\x48\x83\xEB\x09" +# sub ebx,9
		b"\x53" +# push ebx (Image Base)
		b"\x48\x81\xC3" +# add ebx,
		pack("<I",func_offset) +# value
		b"\xFF\xD3" +# call esp
		b"\xc3" # ret
                );

    return bootstrap;


def inject_pe(pe_path,out_name):
    pe_file = get_pe_load(pe_path)

    inject_size = 0
    inject_location = 0

    if get_pe_bit(pe_file):
        reflective_stub = open('resources/stub64.bin', 'rb').read()
    else:
        reflective_stub = open('resources/stub32.bin', 'rb').read()

    cave_size = len(reflective_stub);

    for section in pe_file.sections:
        section_cave_size = section.SizeOfRawData - section.Misc_VirtualSize
        section_cave_location = section.Misc_VirtualSize + section.PointerToRawData
        print("[+] looking for a codecave in %s sizeof %d  offset of %x" % (
        section.Name, section_cave_size, section_cave_location))
        if section_cave_size > cave_size:
            inject_size = section_cave_size
            inject_location = section_cave_location
            break

        if inject_size == 0:
            print("[-] not enough size code cvae found ")
            sys.exit()

    inject_bootstrap = get_inject_bootstrap(pe_file, inject_location)

    pe_file_array = open(pe_path, 'rb').read()
    print("[+] loaded nameof %s" % (pe_path))

    inject_pe_file = inject_bootstrap + pe_file_array[len(inject_bootstrap):inject_location] + reflective_stub + pe_file_array[
                                                                                                       inject_location + len(
                                                                                                           reflective_stub):]
    print("[+] injected offset %x" % (section_cave_location))

    write_pe_file(inject_pe_file,pe_path,out_name)
