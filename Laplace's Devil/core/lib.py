import sys
import pefile
import traceback

def get_pe_load(pe_path):
    try:
        pe_file = pefile.PE(pe_path)
    except Exception as e:
        print(str(e))
        sys.exit()
    return pe_file

def get_pe_bit(pe_file):
    if pe_file.FILE_HEADER.Machine == 0x014c:
        is64 = False
    elif pe_file.FILE_HEADER.Machine ==0x0200 or pe_file.FILE_HEADER.Machine == 0x8664:
        is64 =True
    else:
        print("[-]unknow the format of this pe file")
        sys.exit()

    return is64

def write_pe_file(pe_file,pe_name,out_name=""):
    call_func =traceback.extract_stack()[-2][2]

    if out_name =="":
        if "addit" in call_func:
            out_name = 'addit-' + pe_name
        elif "inject" in call_func:
            out_name = 'inject-' + pe_name
        elif "patch" in call_func:
            out_name = 'patch-' + pe_name


    print("[+] wrote nameof %s" % (out_name))
    open(out_name,'wb').write(pe_file)

