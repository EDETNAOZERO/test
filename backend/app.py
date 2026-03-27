from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!\n")
        else:
            self.send_response(404)
            self.end_headers()

server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
