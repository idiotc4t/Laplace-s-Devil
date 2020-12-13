import sys
import pefile
from struct import pack
from core.lib import *

def patch_help():
    print("usage: python3 <DllPath> <FuncName>\n")
    sys.exit()

def get_func_offset(pe_file, func_name):
    func_rva=0
    if hasattr(pe_file, 'DIRECTORY_ENTRY_EXPORT'):
        for export in pe_file.DIRECTORY_ENTRY_EXPORT.symbols:
            if func_name in str(export.name):
                func_rva = export.address
                break

    if func_rva == 0:
        print("[-] not found function offset in file")
        sys.exit(0)

    offset_va = func_rva - pe_file.get_section_by_rva(func_rva).VirtualAddress
    func_file_offset = offset_va + pe_file.get_section_by_rva(func_rva).PointerToRawData
    func_file_offset -= 9

    return bytes(pack("<I", func_file_offset))


def get_patch_bootstrap(pe_file, func_offset):
    if get_pe_bit(pe_file):
        is64 = True
    else:
        is64 = False


    if is64:
        bootstrap = (
                b"\x4D\x5A"
                b"\x41\x52"
                b"\xe8\x00\x00\x00\x00"
                b"\x5b"
                b"\x48\x81\xC3" + func_offset +
                b"\x55"
                b"\x48\x89\xE5"
                b"\xFF\xD3"
        );

    else:
        bootstrap = (
                b"\x4D"
                b"\x5A"
                b"\x45"
                b"\x52"
                b"\xE8\x00\x00\x00\x00"
                b"\x5A"
                b"\x81\xC2" + func_offset +
                b"\x55"
                b"\x8B\xEC"
                b"\xFF\xD2"
        );
    return bootstrap;


def patch_dll(pe_path, func_name,out_name):

    pe_file = get_pe_load(pe_path)


    func_offset = get_func_offset(pe_file, func_name)
    patch_bootstrap = get_patch_bootstrap(pe_file, func_offset)

    pe_file_array = open(pe_path, 'rb').read()
    print("[+] loaded nameof %s" % (pe_path))

    patch_pe_file = patch_bootstrap + pe_file_array[len(patch_bootstrap):]
    print("[+] patched offset %s" % (func_offset.hex()))

    write_pe_file(patch_pe_file, pe_path, out_name)