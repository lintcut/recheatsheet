import idautils
import idc

string_type_map = {
    0 : "ASCSTR_C",       #              C-string, zero terminated
    1 : "ASCSTR_PASCAL",  #              Pascal-style ASCII string (length byte)
    2 : "ASCSTR_LEN2",    #              Pascal-style, length is 2 bytes
    3 : "ASCSTR_UNICODE", #              Unicode string
    4 : "ASCSTR_LEN4",    #              Delphi string, length is 4 bytes
    5 : "ASCSTR_ULEN2",   #              Pascal-style Unicode, length is 2 bytes
    6 : "ASCSTR_ULEN4",   #              Pascal-style Unicode, length is 4 bytes
}

def main():
    #Do not use default set up, we'll call setup().
    s = idautils.Strings(default_setup = False)
    # we want C & Unicode strings, and *only* existing strings.
    s.setup(strtypes=[ida_nalt.STRTYPE_C, ida_nalt.STRTYPE_C_16], ignore_instructions = True, display_only_existing_strings = True)

    #loop through strings
    for i, v in enumerate(s):                
        if not v:
            print("Failed to retrieve string at index {}".format(i))
        else:
            print("[{}] ea: {:#x} ; length: {}; type: {}; '{}'".format(i, v.ea, v.length, string_type_map.get(v.strtype, None), str(v)))

if __name__ == "__main__":
    main()