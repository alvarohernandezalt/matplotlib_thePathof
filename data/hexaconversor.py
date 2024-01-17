def string_to_hex(string):
    hex_code = ""
    for char in string:
        hex_code += hex(ord(char))[2:]
    return hex_code

# Example usage
input_string = "almena"
hex_code = string_to_hex(input_string)
print(hex_code)
