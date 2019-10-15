from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "<h1>Web Page</h1>Content"
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('Server starting...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print('Server live...')
    print(' - ctrl-c to stop')
    httpd.serve_forever()

run()
