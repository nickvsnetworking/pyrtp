#160ms between packets
#Even Ports
#G7.11A - 214 bytes on the wire
#16384-32767
#RTCP is port number + 1 (Always odd as RTCP as RTP is always even)
import pyrtp
import random
import sys
import socket
import time

lowest_port = 16384         #Both these values must be even
max_port = 32766            #Even this one... Trust me.
destination = "1.2.3.4"
packets = 3
packetization = 150         #Packetization in ms

port = (random.randint(lowest_port/2,max_port/2)*2)       #Selects our RTP port by picking a random number between half the highest port value and half the lowest, and multiplying it by 2 to always get an even number
print("Selected Port is: " + str(port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(('0.0.0.0', 1447))


sequence_number = random.randint(1,9999)
time_int = random.randint(1,9999)

while packets != 0:


    packets = packets - 1
    time_int = time_int + 1
    sequence_number = sequence_number + 1
    rtp_params = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : sequence_number, 'timestamp' : time_int, 'ssrc' : 185755418}

    header_hex = pyrtp.GenerateRTPpacket(rtp_params)
    
    sock.sendto(bytes.fromhex(header_hex), (destination, port))
    
    time.sleep(0.0150)
sock.close()

