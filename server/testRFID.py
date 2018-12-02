import struct

a = 98*10

bbyte = struct.pack('H',a)
print(bbyte)