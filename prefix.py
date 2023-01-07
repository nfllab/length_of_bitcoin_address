#!/usr/bin/env python3

# verifying https://en.bitcoin.it/wiki/List_of_address_prefixes

import base58
import prettytable

t = prettytable.PrettyTable()
t.field_names = ["Decimal version", "Leading symbol", "Address length"]
t.align = "r"
t.set_style(prettytable.SINGLE_BORDER)

last_len_str = ""
last_symbol_str = ""
last_version = -1

for version in range(1, 256):
    lo = bytes([version]) + 20 * b"\x00"
    lo_b58 = base58.b58encode_check(lo)
    hi = bytes([version]) + 20 * b"\xff"
    hi_b58 = base58.b58encode_check(hi)
    lo_len = len(lo_b58)
    hi_len = len(hi_b58)
    if lo_len != hi_len:
        len_str = f"{lo_len} to {hi_len}"
    else:
        len_str = f"{lo_len}"
    lo_symbol = chr(lo_b58[0])
    hi_symbol = chr(hi_b58[0])
    if lo_symbol != hi_symbol:
        symbol_str = f"{lo_symbol} to {hi_symbol}"
    else:
        symbol_str = f"{lo_symbol}"
    if last_len_str != len_str or last_symbol_str != symbol_str:
        if last_version != -1:
            version_str = f"{last_version}"
            if last_version != version - 1:
                version_str += f"-{version-1}"
            t.add_row([f"{version_str}", last_symbol_str, last_len_str])
        last_version = version
        last_symbol_str = symbol_str
        last_len_str = len_str

t.add_row([f"{last_version}-{version}", last_symbol_str, last_len_str])

print(t)
