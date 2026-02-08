from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "message": "Hello from Romans8! 🚀",
            "time": "It's around 11 PM CST on Feb 7, 2026",
            "from": "Your Vercel Python test"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
