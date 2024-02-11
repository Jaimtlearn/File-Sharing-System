try:
    import http.server
    import socket
    import socketserver
    import webbrowser
    import pyqrcode
    from pyqrcode import QRCode
    import png
    import os
except :
    print("Error while loading imports")

print("Import Successful")

Port = 8000

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive')
# print(desktop)
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler # http server object

hostname = socket.gethostname() # host name or pc name

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80)) # laddr = local address of socket, raddr = remote address of socket
# print(s.getsockname()) # returns socket ip 
link = "http://" + s.getsockname()[0] + ":" + str(Port)

URL = pyqrcode.create(link) # Creates qr code

URL.svg("Qr.svg",scale = 10) # opens qr in browser

webbrowser.open('Qr.svg')

with socketserver.TCPServer(("",Port),Handler) as httpd:
    print(f"Listening at Port : {Port}")
    print(f"Browser Ip (type this) : {link}")
    print("Or use QR Code")
    httpd.serve_forever()
