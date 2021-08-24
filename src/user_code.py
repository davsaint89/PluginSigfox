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
    '<f' for little endian
    '>f' for big endian
    4 bytesminimum requiered for unpacking
    '''
    temp = int(hex_array[0])
    lat = round(struct.unpack('>f', hex_array[1:5])[0],2) 
    ln = round(struct.unpack('>f', hex_array[5:10])[0],2) 

    payload['temperatura'] = {'value': temp, 'context':{'lat':lat, 'ln':ln}}

    return payload

