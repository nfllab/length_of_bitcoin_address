#!/usr/bin/env python3

import base58
import prettytable

t = prettytable.PrettyTable()
t.field_names = ["Leading zeros", "Maximum base58 digits", "Maximum total length"]
t.align = "r"
t.set_style(prettytable.SINGLE_BORDER)

for zeros in range(21, 0, -1):
    others = 21 - zeros
    input_max = zeros * b"\x00" + others * b"\xff"
    length_max = len(base58.b58encode_check(input_max))
    t.add_row([zeros, length_max - zeros, length_max])

print(t)
