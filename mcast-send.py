import socket
import sys
mcastgroup = '224.3.29.71'
message = 'Multicast Operationional on ' + mcastgroup
multicast_group = (mcastgroup, 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)
try:
    i = 0
    while i < 10:
        # Send data to the multicast group
        print(sys.stderr, 'sending "%s"' % message)
        sent = sock.sendto(message.encode(), multicast_group)

        # Look for responses from all recipients
        while True:
            print(sys.stderr, 'waiting to receive')
            try:
                data, server = sock.recvfrom(16)
            except socket.timeout:
                print(sys.stderr, 'timed out, no more responses')
                i +=1
                break
            else:
                print(sys.stderr, 'received "%s" from %s' % (data, server))

finally:
    print(sys.stderr, 'closing socket')
    sock.close()