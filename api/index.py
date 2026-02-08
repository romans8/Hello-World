# api/index.py
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {
            "message": "Hello from Romans8! 🚀",
            "time": "Around 11:30 PM CST on Feb 7, 2026",
            "status": "This is your first working Vercel Python endpoint",
            "path": self.path  # Shows the requested URL for testing
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))
