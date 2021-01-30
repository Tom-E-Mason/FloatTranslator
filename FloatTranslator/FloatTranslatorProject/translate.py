
import argparse as ap
import struct
import bitarray as ba
import bitarray.util as bau

HEX = "hex"
BIN = "bin"
FLT = "flt"

def parse_command_line():
    parser = ap.ArgumentParser(description = "convert between hex and floating point")
    parser.add_argument("input_number",
                        help = ("prepend hexadecimal input with \"0x\" and "
                                "binary input with \"0b\""))
    parser.add_argument("output_format",
                        choices = [HEX, BIN, FLT],
                        help = ("choose output format from hexadecimal, "
                                "binary and floating point"))
    parser.add_argument("endianness",
                        choices = ["big", "little"],
                        help = "endianness  of hexadecimal or binary number")


    args = parser.parse_args()

    return args.input_number, args.output_format, args.endianness

def get_endian_tag(endianness):
    if endianness == "big":
        return ">"
    elif endianness == "little":
        return "<"
    else:
        SystemError("invalid endianness")

def reverse_hex_bytes(hex_num):
    for i in range(2, len(hex_num), 2):
        byte = hex_num[i:i+2]
        hex_num = hex_num.replace(byte, byte[::-1])
    return hex_num

def hex_big_to_little(hex_num):
    hex_num = hex_num.replace(hex_num[2:], hex_num[len(hex_num):1:-1])

    hex_num = reverse_hex_bytes(hex_num)
    return hex_num

def hex_to_float(hex_num, endianness):
    
    endian_tag = get_endian_tag(endianness)
    return struct.unpack(endian_tag + "f", bytes.fromhex(hex_num))[0]
    
def float_to_hex(flt_num, endianness):
    hex_num = hex(struct.unpack("I", struct.pack("f", float(flt_num)))[0])

    if endianness == "little":
        hex_num = hex_big_to_little(hex_num)

    return hex_num

def bin_to_float(bin_num, endianness):
    bs = ba.bitarray(bin_num, endian = endianness)

    hex_num = bau.ba2hex(bs)

    if endianness == "little":
        hex_num = "0x" + hex_num
        hex_num = reverse_hex_bytes(hex_num)
        hex_num = hex_num.replace("0x", "")
        #0b1111001101011101  
    return hex_to_float(hex_num, endianness)

def float_to_bin(flt_num, endianness):
    endian_tag = get_endian_tag(endianness)

    int_representation = struct.unpack(endian_tag + "I", struct.pack(endian_tag + "f", float(flt_num)))[0]
    bs = ba.bitarray(format(int_representation, "032b"), endianness)
    return bs.to01()

def hex_to_bin(hex_num, endianness):
    bin_num = bin(int(hex_num, 16))

    if endianness == "little":
        bin_num = bin_num.replace(bin_num[2:], bin_num[len(bin_num):1:-1])

    extra_zs = ( len(bin_num) - 2) % 8
    zs = format(0, "0" + str(extra_zs))
    bin_num = bin_num[:2] + zs + bin_num[2:] 

    with_spaces = ""
    for i in range((len(bin_num) - 2) // 8):
        with_spaces = " " + bin_num[len(bin_num) - 8 * (i + 1):len(bin_num) - 8 * i] + with_spaces

    with_spaces = bin_num[0:2] + with_spaces

    return with_spaces

def bin_to_hex(bin_num, endianness):
    bs = ba.bitarray(bin_num)
    hex_num = bau.ba2hex(bs)
    hex_num = "0x" + hex_num

    if endianness == "little":
        hex_num = hex_big_to_little(hex_num)
    

    return hex_num