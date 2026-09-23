from http.server import HTTPServer, BaseHTTPRequestHandler

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
       # Added a second line to the greeting
        message = "<h1>Greetings from Farwa!</h1><p>Welcome to my containerized app assignment!</p>"
        self.wfile.write(message.encode('utf-8'))


if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, GreeterHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()