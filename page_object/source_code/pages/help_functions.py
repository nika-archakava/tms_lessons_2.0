from functools import reduce


def from_rgba_to_hex(rgba_string):
    rgba_list = rgba_string[5:-1].split(', ')
    hex_list = list(map(lambda x: hex(int(x))[2:].zfill(2), rgba_list[:3]))
    hex_string = '#' + reduce(lambda x, y: x + y, hex_list)
    if float(rgba_list[3]) < 1:
        hex_string += hex(int(float(rgba_list[3]) * 255))[2:].zfill(2)
    return hex_string