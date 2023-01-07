#!/usr/bin/env python3

import base58
import prettytable

t = prettytable.PrettyTable()
t.field_names = ["Leading zeros", "Minimum base58 digits", "Minimum total length"]
t.align = "r"
t.set_style(prettytable.SINGLE_BORDER)

for zeros in range(21, 0, -1):
    others = 21 - zeros
    if others > 0:
        input_min = zeros * b"\x00" + b"\x01" + (others - 1) * b"\x00"
    else:
        input_min = zeros * b"\x00"
    length_min = len(base58.b58encode_check(input_min))
    t.add_row([zeros, length_min - zeros, length_min])

print(t)
