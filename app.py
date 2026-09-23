from http.server import HTTPServer, BaseHTTPRequestHandler

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Replace "Your Name" with your actual name
        message = "<h1>Hello from Your Name!</h1>"
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, GreeterHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()