import struct

def format_payload(args):
  hex_array = bytearray.fromhex(args["data"])
  payload = decode_data(hex_array)
  return payload
  
def decode_data(hex_array):
  payload = {}
  '''
  Put your decoding function here.
  We recommend using Python struct package or bitwise operations 
  to operate the binary data
  '''
  return payload