
import translate as tl

def main():
    input, output_format, endianness = tl.parse_command_line()

    print ("\nInput: ", input)

    if input.startswith("0x"):
        input = input.replace("0x", "")
        if output_format == tl.FLT:
            output = tl.hex_to_float(input, endianness)
        elif output_format == tl.BIN:
            output = tl.hex_to_bin(input, endianness)
        elif output_format == tl.HEX:
            output = input
        else:
            print("invalid output format")
    elif input.startswith("0b"):
        input = input.replace("0b", "")
        if output_format == tl.FLT:
            output = tl.bin_to_float(input, endianness)
        elif output_format == tl.HEX:
            output = tl.bin_to_hex(input, endianness)
    else:
        if output_format == tl.HEX:
            output = tl.float_to_hex(input, endianness)
        elif output_format == tl.BIN:
            output = tl.float_to_bin(input, endianness)
        elif output_format == tl.FLT:
            output = input
        
        else:
            print("invalid output format")

    print("\nOutput: ", output)

if __name__ == "__main__":
    main()