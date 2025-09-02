# run_local_server.py
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Change working dir to this script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"Serving at {url}")
    webbrowser.open(url)
    httpd.serve_forever()
