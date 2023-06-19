
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


# from flask import Flask, render_template_string

# app = Flask(__name__)

# @app.route('/')
# def display_variable():
#     my_variable = "Hello, World!"
#     template = "<h1>{{ variable }}</h1>"
#     return render_template_string(template, variable=my_variable)

# if __name__ == '__main__':
#     app.run()
