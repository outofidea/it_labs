from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import urllib.parse

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Default to index.html for root path
        if path == '/':
            path = '/index.html'
        
        # Remove leading slash for file path
        file_path = path[1:] if path.startswith('/') else path
        
        try:
            # Try to open and read the requested file
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Determine content type based on file extension
            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            elif file_path.endswith('.png'):
                content_type = 'image/png'
            elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                content_type = 'image/jpeg'
            elif file_path.endswith('.gif'):
                content_type = 'image/gif'
            else:
                content_type = 'text/plain'
            
            # Send successful response
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content)
            
        except FileNotFoundError:
            # Send 404 error if file not found
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>404 - Page Not Found</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; }
                    h1 { color: #e74c3c; }
                </style>
            </head>
            <body>
                <h1>404 - Page Not Found</h1>
                <p>The requested file could not be found on this server.</p>
                <a href="/">Go back to home</a>
            </body>
            </html>
            """
            self.wfile.write(bytes(error_html, 'utf-8'))
        
        except Exception as e:
            # Send 500 error for other exceptions
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>500 - Internal Server Error</title>
            </head>
            <body>
                <h1>500 - Internal Server Error</h1>
                <p>An error occurred: {str(e)}</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(error_html, 'utf-8'))

def run_server(port=8080):
    # Bind to all network interfaces to allow local network access
    server_address = ('10.0.6.243', port)
    httpd = HTTPServer(server_address, WebHandler)
    
    # Get local IP address
    import socket
    hostname = socket.gethostname()
    print(hostname)
    local_ip = "" \
    "10.0.6.243"
    
    print(f"Server running and accessible from:")
    print(f"- This computer: http://localhost:{port}")
    print(f"- Other devices on network: http://{local_ip}:{port}")
    print(f"")
    print(f"Share http://{local_ip}:{port} with others on your WiFi!")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
