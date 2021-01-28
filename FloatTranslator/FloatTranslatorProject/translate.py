
import argparse as ap

hex = "hex"
bin = "bin"
flt = "flt"
dbl = "dbl"

def parse_command_line():
    parser = ap.ArgumentParser(description = "convert between hex and floating point")
    parser.add_argument("input_number",
                        help = ("prepend hexadecimal input with \"0x\" and "
                                "binary input with \"0b\""))
    parser.add_argument("output_format",
                        choices = [hex, bin, flt, dbl],
                        help = ("choose output format from hexadecimal, "
                                "binary, single precision floating point "
                                "and double precision floating point"))
    parser.add_argument("endianness of hexadecimal or binary number",
                        choices = ["big", "little"],
                        help = "endianness")


    args = parser.parse_args()

    return args.input_number, args.output_format, args.endianness