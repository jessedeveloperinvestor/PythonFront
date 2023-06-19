from http.server import SimpleHTTPRequestHandler, HTTPServer

# Set the port number for the server
port = 8000

# Define the directory containing your frontend files
directory = '.'  # Replace '.' with the directory path containing your frontend files

# Create an HTTP server with the SimpleHTTPRequestHandler
httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)

# Start the server
print(f'Starting server on port {port}...')
httpd.serve_forever()
