import http.server
import socketserver
import logging

# Set up logging configuration
logging.basicConfig(filename='requests.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class LoggingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log the request path
        logging.info(f'Received GET request for: {self.path}')
        # Call superclass to handle the request
        super().do_GET()

    def do_POST(self):
        # Log the request path and content length
        content_length = int(self.headers['Content-Length'])  # Get content length
        post_data = self.rfile.read(content_length)  # Read the data
        logging.info(f'Received POST request for: {self.path} with data: {post_data.decode()}')
        # Respond to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Received POST request!')

# Set the port for the server
PORT = 8081

# Create a TCP server and bind it to the handler
with socketserver.TCPServer(("", PORT), LoggingHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
