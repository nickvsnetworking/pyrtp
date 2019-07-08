

def GenerateRTPpacket(rtp_params):

    #Example Usage:
    ##payload = 'd5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'
    ##rtp_params = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : 306, 'timestamp' : 306, 'ssrc' : 185755418, 'payload' : payload}
    ##GenerateRTPpacket(rtp_params)             #Generates hex to send down the wire


    
    #The first twelve octets are present in every RTP packet, while the list of CSRC identifiers is present only when inserted by a mixer.
    #This data is converted into binary strings and concatenated together

    #Generate first byte of header as binary string:
    version = str(format(rtp_params['version'], 'b').zfill(2))                  #RFC189 Version (Typically 2)
    padding = str(rtp_params['padding'])                                        #Padding (Typically false (0))
    extension = str(rtp_params['extension'])                                    #Extension - Disabled
    csi_count = str(format(rtp_params['csi_count'], 'b').zfill(4))              #Contributing Source Identifiers Count (Typically 0)
    byte1 = format(int((version + padding + extension + csi_count), 2), 'x').zfill(2)                           #Convert binary values to an int then format that as hex with 2 bytes of padding if requiredprint(byte1)
    

    #Generate second byte of header as binary string:
    marker = str(rtp_params['marker'])                                          #Marker (Typically false)
    payload_type = str(format(rtp_params['payload_type'], 'b').zfill(7))        #7 bit Payload Type (From https://tools.ietf.org/html/rfc3551#section-6)
    byte2 = format(int((marker + payload_type), 2), 'x').zfill(2)                           #Convert binary values to an int then format that as hex with 2 bytes of padding if required


    
    sequence_number = format(rtp_params['sequence_number'], 'x').zfill(4)                               #16 bit sequence number (Starts from a random position and incriments per packet)
    
    timestamp = format(rtp_params['timestamp'], 'x').zfill(8)             #32 bit timestamp       (Typically incrimented by the fixed time between packets)

    
    ssrc = str(format(rtp_params['ssrc'], 'x').zfill(8))                       #SSRC 32 bits           (Typically randomly generated for each stream for uniqueness)

    payload = rtp_params['payload']
    

    packet = byte1 + byte2 + sequence_number + timestamp + ssrc + payload
    #print(packet)
    return packet


    

