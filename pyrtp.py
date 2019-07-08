#160ms between packets
#Even Ports
#G7.11A - 214 bytes on the wire
#16384-32767
#RTCP is port number + 1 (Always odd as RTCP as RTP is always even)


def GenerateRTPpacket(rtp_params):
    #The first twelve octets are present in every RTP packet, while the list of CSRC identifiers is present only when inserted by a mixer.
    #This data is converted into binary strings and concatenated together
    version = str(format(rtp_params['version'], 'b').zfill(2))                  #RFC189 Version (Typically 2)
    padding = str(rtp_params['padding'])                                        #Padding (Typically false (0))
    extension = str(rtp_params['extension'])                                    #Extension - Disabled
    csi_count = str(format(rtp_params['csi_count'], 'b').zfill(4))              #Contributing Source Identifiers Count (Typically 0)
    marker = str(rtp_params['marker'])                                          #Marker (Typically false)
    payload_type = str(format(rtp_params['payload_type'], 'b').zfill(7))        #7 bit Payload Type (From https://tools.ietf.org/html/rfc3551#section-6)
    sequence_number = ("{0:b}".format(rtp_params['sequence_number']).zfill(16)) #16 bit sequence number (Starts from a random position and incriments per packet)
    timestamp = ("{0:b}".format(rtp_params['timestamp']).zfill(32))             #32 bit timestamp       (Typically incrimented by the fixed time between packets)
    ssrc = str(format(rtp_params['ssrc'], 'b').zfill(32))                       #SSRC 32 bits           (Typically randomly generated for each stream for uniqueness)

    payload = ("1".zfill(260))                      #Fill payload and pad with 160 chars of nothing.

    packets = 1

 
    headers = version + padding + extension + csi_count + marker + payload_type + sequence_number + timestamp + ssrc
    print(headers)
    headers = headers + payload

    position = 0
    octetcount = 1
    header_hex = ""

    while position < 256:
        octet = headers[position:(position+8)]
        octet_hex = hex(int(octet,2))

        #Format Hex from 0x8 to 08
        octet_hex = octet_hex.split("x")[1].zfill(2)
        
        print("Octet " + str(octetcount).zfill(2) + ": " + str(octet) + "\t\tHex: " + octet_hex)
        
        position = position + 8
        octetcount = octetcount + 1
        header_hex = header_hex + "" + octet_hex

    print(header_hex)
    return header_hex

        
    

##rtp_params = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : 306, 'timestamp' : 306, 'ssrc' : 185755418}
##header_gen = GenerateRTPpacket(rtp_params)
##header_expected = '80080132000001320b12671a0000000000000000000000000000000000000001'
##if header_gen != header_expected:
##    print("Mismatch")
##else:
##    print("Match")

