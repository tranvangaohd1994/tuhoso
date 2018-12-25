
import struct

byteKC = struct.pack('B',60)
arr = [1,2,3,4]
arr[1] = byteKC[0]
dtSend = b'\xaa\xaa'+ bytearray(arr)+ b'\x00\x00'
print(byteKC , arr, dtSend)