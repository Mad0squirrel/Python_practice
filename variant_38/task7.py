def main(x):
    A = (x & 0b00000000000000000000000000000001) << 27
    B = (x & 0b00000000000000000000000000000010) << 27
    C = (x & 0b00000000000000111111111111111100) << 1
    D = (x & 0b00000000000011000000000000000000) << 11
    E = (x & 0b00000000000100000000000000000000) << 11
    F = (x & 0b00011111111000000000000000000000) >> 2
    G = (x & 0b11100000000000000000000000000000) >> 29
    return E | D | B | A | F | C | G


print(hex(main(0x6d29d607)))
print(hex(main(0x1397af7a)))
print(hex(main(0xff576dbc)))
print(hex(main(0xc180ed05)))
print(hex(main(0xc546ff07)))