import socket

print("[+] Fake NATS Server listening on 0.0.0.0:4444")
s = socket.socket(); s.bind(("0.0.0.0", 4222)); s.listen(5)

while True:
    client, addr = s.accept()
    print(f"\n[+] Connection from {addr}")
    
    client.sendall(b'INFO {"server_id":"FAKE","version":"2.11.0","auth_required":true}\r\n')
    data = client.recv(1024)
    print("\n[+]Received:")
    print(data.decode())
    client.close()
