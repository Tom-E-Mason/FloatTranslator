
import translate as tl

def main():
    input, output_format, endianness = tl.parse_command_line()

    print(input)
    print(output_format)
    print(endianness)

    input_format = ""
    if input.find("0x") == 0:
        input_format = hex
    elif input.find("0b") == 0:
        input_format = bin
    else:
        input_format = flt # work out doubles later

    print(input_format)

if __name__ == "__main__":
    main()